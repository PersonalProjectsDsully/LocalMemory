"""
Moby Thesaurus Integration for Local Knowledgebase System

This module provides comprehensive integration of the Moby Thesaurus,
containing over 30,000 root words and 2.5 million synonyms.
"""

import requests
import json
import pickle
import os
from pathlib import Path
from collections import defaultdict
import time
from typing import List, Set, Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MobyThesaurusDownloader:
    """Handles downloading and initial processing of Moby Thesaurus"""
    
    def __init__(self, data_dir: str = "data/thesaurus"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.raw_file = self.data_dir / "moby-thesaurus-raw.txt"
        self.processed_file = self.data_dir / "moby-thesaurus-processed.pkl"
        self.index_file = self.data_dir / "moby-thesaurus-index.json"
        
    def download_thesaurus(self, force: bool = False) -> bool:
        """Download the Moby Thesaurus file"""
        if self.raw_file.exists() and not force:
            logger.info(f"Thesaurus already downloaded at {self.raw_file}")
            return True
            
        logger.info("Downloading Moby Thesaurus...")
        
        # The correct URL for the thesaurus file
        url = "https://raw.githubusercontent.com/words/moby/master/words.txt"
        
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Save raw file
            with open(self.raw_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            logger.info(f"Downloaded {len(response.text)} bytes to {self.raw_file}")
            return True
            
        except requests.RequestException as e:
            logger.error(f"Error downloading thesaurus: {e}")
            
            # Alternative: Try the thesaurus-specific file
            alt_url = "https://raw.githubusercontent.com/words/moby/master/m_thesaurus.txt"
            logger.info(f"Trying alternative source: {alt_url}")
            
            try:
                response = requests.get(alt_url, timeout=30)
                response.raise_for_status()
                
                with open(self.raw_file, 'w', encoding='utf-8') as f:
                    f.write(response.text)
                
                return True
            except Exception as e2:
                logger.error(f"Failed to download from alternative source: {e2}")
                
                # Try another alternative
                final_url = "https://www.gutenberg.org/files/3202/files/mthesaur.txt"
                logger.info(f"Trying final alternative: {final_url}")
                
                try:
                    response = requests.get(final_url, timeout=30)
                    response.raise_for_status()
                    
                    with open(self.raw_file, 'w', encoding='utf-8') as f:
                        f.write(response.text)
                    
                    return True
                except:
                    logger.error("Failed to download from all sources")
                    return False


class MobyThesaurusProcessor:
    """Process raw Moby data into efficient data structures"""
    
    def __init__(self, downloader: MobyThesaurusDownloader):
        self.downloader = downloader
        self.thesaurus = {}
        self.reverse_index = defaultdict(set)
        self.word_stats = {}
        
    def process_raw_file(self) -> Dict[str, List[str]]:
        """Process the raw thesaurus file into a structured format"""
        if not self.downloader.raw_file.exists():
            raise FileNotFoundError(f"Raw file not found: {self.downloader.raw_file}")
        
        logger.info("Processing Moby Thesaurus...")
        start_time = time.time()
        
        thesaurus = {}
        total_synonyms = 0
        max_synonyms = 0
        
        with open(self.downloader.raw_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f):
                if line_num % 1000 == 0 and line_num > 0:
                    logger.info(f"Processing line {line_num}...")
                
                line = line.strip()
                if not line:
                    continue
                
                # Split by comma - first word is the root word
                words = [w.strip() for w in line.split(',')]
                if len(words) < 2:
                    continue
                
                root_word = words[0].lower()
                synonyms = [w.lower() for w in words[1:] if w.strip()]
                
                # Remove duplicates while preserving order
                seen = set()
                unique_synonyms = []
                for syn in synonyms:
                    if syn not in seen and syn != root_word:
                        seen.add(syn)
                        unique_synonyms.append(syn)
                
                thesaurus[root_word] = unique_synonyms
                total_synonyms += len(unique_synonyms)
                max_synonyms = max(max_synonyms, len(unique_synonyms))
                
                # Build reverse index for bidirectional lookup
                for synonym in unique_synonyms:
                    self.reverse_index[synonym].add(root_word)
        
        # Calculate statistics
        self.word_stats = {
            'total_root_words': len(thesaurus),
            'total_synonyms': total_synonyms,
            'average_synonyms_per_word': total_synonyms / len(thesaurus) if thesaurus else 0,
            'max_synonyms': max_synonyms,
            'processing_time': time.time() - start_time
        }
        
        logger.info(f"Processed {len(thesaurus)} root words with {total_synonyms} total synonyms")
        logger.info(f"Average synonyms per word: {self.word_stats['average_synonyms_per_word']:.2f}")
        logger.info(f"Processing took {self.word_stats['processing_time']:.2f} seconds")
        
        self.thesaurus = thesaurus
        return thesaurus
    
    def save_processed_data(self):
        """Save processed data for faster loading"""
        logger.info("Saving processed data...")
        
        # Save main thesaurus as pickle for fast loading
        with open(self.downloader.processed_file, 'wb') as f:
            pickle.dump({
                'thesaurus': self.thesaurus,
                'reverse_index': dict(self.reverse_index),
                'stats': self.word_stats,
                'version': '1.0'
            }, f)
        
        # Save index as JSON for inspection
        index_data = {
            'stats': self.word_stats,
            'sample_entries': dict(list(self.thesaurus.items())[:10]),
            'total_words': len(self.thesaurus)
        }
        
        with open(self.downloader.index_file, 'w') as f:
            json.dump(index_data, f, indent=2)
        
        logger.info(f"Saved processed data to {self.downloader.processed_file}")


class MobyThesaurusExpander:
    """Main class for query expansion using Moby Thesaurus"""
    
    def __init__(self, data_dir: str = "data/thesaurus"):
        self.downloader = MobyThesaurusDownloader(data_dir)
        self.processor = MobyThesaurusProcessor(self.downloader)
        self.thesaurus = {}
        self.reverse_index = {}
        self.initialized = False
        
    def initialize(self, force_download: bool = False, force_process: bool = False):
        """Initialize the thesaurus, downloading if necessary"""
        
        # Try to load processed data first
        if not force_process and self.downloader.processed_file.exists():
            logger.info("Loading pre-processed thesaurus...")
            try:
                with open(self.downloader.processed_file, 'rb') as f:
                    data = pickle.load(f)
                    self.thesaurus = data['thesaurus']
                    self.reverse_index = data['reverse_index']
                    self.initialized = True
                    logger.info(f"Loaded {len(self.thesaurus)} words from cache")
                    return
            except Exception as e:
                logger.error(f"Error loading processed data: {e}")
        
        # Download if necessary
        if not self.downloader.raw_file.exists() or force_download:
            if not self.downloader.download_thesaurus(force_download):
                raise RuntimeError("Failed to download thesaurus")
        
        # Process the raw file
        self.processor.process_raw_file()
        self.processor.save_processed_data()
        
        self.thesaurus = self.processor.thesaurus
        self.reverse_index = self.processor.reverse_index
        self.initialized = True
    
    def get_synonyms(self, word: str, max_results: int = 10) -> List[str]:
        """Get synonyms for a single word"""
        if not self.initialized:
            self.initialize()
        
        word = word.lower().strip()
        
        # Direct lookup
        synonyms = self.thesaurus.get(word, [])[:max_results]
        
        # If no direct match, try reverse lookup
        if not synonyms and word in self.reverse_index:
            # Word might be a synonym of other root words
            root_words = list(self.reverse_index[word])[:3]
            for root in root_words:
                synonyms.extend(self.thesaurus.get(root, [])[:5])
            
            # Remove the original word and duplicates
            synonyms = list(dict.fromkeys(syn for syn in synonyms if syn != word))[:max_results]
        
        return synonyms
    
    def expand_query(self, query: str, max_per_word: int = 5, 
                     context_weight: bool = True) -> Dict[str, List[str]]:
        """Expand a full query string"""
        if not self.initialized:
            self.initialize()
        
        # Tokenize query (simple version - enhance with NLTK/spaCy if needed)
        words = query.lower().split()
        
        expansions = {}
        
        for word in words:
            # Skip common stop words
            if word in {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}:
                continue
            
            synonyms = self.get_synonyms(word, max_per_word)
            
            if context_weight and len(words) > 1:
                # Score synonyms based on relevance to other query words
                scored_synonyms = []
                for syn in synonyms:
                    score = self._context_score(syn, words, word)
                    scored_synonyms.append((syn, score))
                
                # Sort by score and take top results
                scored_synonyms.sort(key=lambda x: x[1], reverse=True)
                synonyms = [syn for syn, _ in scored_synonyms[:max_per_word]]
            
            if synonyms:
                expansions[word] = synonyms
        
        return expansions
    
    def _context_score(self, synonym: str, query_words: List[str], 
                       original_word: str) -> float:
        """Score a synonym based on context relevance"""
        score = 0.0
        
        # Check if synonym appears in thesaurus entries of other query words
        for word in query_words:
            if word != original_word and word in self.thesaurus:
                if synonym in self.thesaurus[word]:
                    score += 1.0
        
        # Check reverse relationships
        if synonym in self.reverse_index:
            related_roots = self.reverse_index[synonym]
            for word in query_words:
                if word in related_roots:
                    score += 0.5
        
        return score
    
    def health_check(self) -> Dict[str, any]:
        """Check the health of the thesaurus"""
        return {
            'initialized': self.initialized,
            'total_words': len(self.thesaurus),
            'total_reverse_entries': len(self.reverse_index),
            'cache_exists': self.downloader.processed_file.exists(),
            'raw_file_exists': self.downloader.raw_file.exists()
        }


class CachedMobyThesaurus:
    """Cached version with performance optimizations"""
    
    def __init__(self, cache_size: int = 10000):
        self.thesaurus = MobyThesaurusExpander()
        self.cache = {}
        self.cache_size = cache_size
        self.access_count = defaultdict(int)
        self.initialized = False
    
    def initialize(self, **kwargs):
        """Initialize the underlying thesaurus"""
        try:
            self.thesaurus.initialize(**kwargs)
            self.initialized = True
            logger.info("CachedMobyThesaurus initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize CachedMobyThesaurus: {e}")
            self.initialized = False
        
    def get_synonyms_cached(self, word: str, max_results: int = 10) -> List[str]:
        """Get synonyms with caching"""
        
        cache_key = f"{word}:{max_results}"
        
        # Check cache
        if cache_key in self.cache:
            self.access_count[cache_key] += 1
            return self.cache[cache_key]
        
        # Get from thesaurus
        synonyms = self.thesaurus.get_synonyms(word, max_results)
        
        # Add to cache with LRU eviction
        if len(self.cache) >= self.cache_size:
            # Remove least recently used
            lru_key = min(self.cache.keys(), 
                         key=lambda k: self.access_count.get(k, 0))
            del self.cache[lru_key]
            del self.access_count[lru_key]
        
        self.cache[cache_key] = synonyms
        self.access_count[cache_key] = 1
        
        return synonyms
    
    def preload_common_words(self, word_list: List[str]):
        """Preload cache with common words for better performance"""
        logger.info(f"Preloading {len(word_list)} common words...")
        
        for word in word_list:
            self.get_synonyms_cached(word)
        
        logger.info(f"Cache now contains {len(self.cache)} entries")
    
    def get_synonyms(self, word: str, max_results: int = 10) -> List[str]:
        """Get synonyms (delegate to cached version)"""
        return self.get_synonyms_cached(word, max_results)
    
    def expand_query(self, query: str, max_per_word: int = 5, context_weight: bool = True):
        """Expand query using underlying thesaurus"""
        return self.thesaurus.expand_query(query, max_per_word, context_weight)
    
    def health_check(self):
        """Health check for cached thesaurus"""
        base_health = self.thesaurus.health_check()
        base_health['cache_info'] = {
            'cache_size': len(self.cache),
            'max_cache_size': self.cache_size,
            'cache_hits': sum(self.access_count.values())
        }
        return base_health


class RobustMobyThesaurus(MobyThesaurusExpander):
    """Production-ready version with comprehensive error handling"""
    
    def __init__(self, data_dir: str = "data/thesaurus", 
                 fallback_file: Optional[str] = None):
        super().__init__(data_dir)
        self.fallback_file = fallback_file
        self.error_log = []
        
    def initialize(self, force_download: bool = False, 
                  force_process: bool = False, 
                  max_retries: int = 3):
        """Initialize with retry logic and fallbacks"""
        
        for attempt in range(max_retries):
            try:
                super().initialize(force_download, force_process)
                return
            except Exception as e:
                self.error_log.append({
                    'timestamp': time.time(),
                    'attempt': attempt + 1,
                    'error': str(e)
                })
                
                if attempt < max_retries - 1:
                    logger.warning(f"Initialization attempt {attempt + 1} failed, retrying...")
                    time.sleep(2 ** attempt)  # Exponential backoff
        
        # All retries failed, try fallback
        if self.fallback_file and os.path.exists(self.fallback_file):
            logger.info(f"Loading from fallback file: {self.fallback_file}")
            self._load_fallback()
        else:
            # Initialize with empty thesaurus
            logger.warning("WARNING: Initializing with empty thesaurus")
            self.thesaurus = {}
            self.reverse_index = {}
            self.initialized = True
    
    def _load_fallback(self):
        """Load from a fallback file"""
        try:
            with open(self.fallback_file, 'r') as f:
                fallback_data = json.load(f)
                self.thesaurus = fallback_data.get('thesaurus', {})
                self.reverse_index = fallback_data.get('reverse_index', {})
                self.initialized = True
                logger.info(f"Loaded {len(self.thesaurus)} words from fallback")
        except Exception as e:
            logger.error(f"Failed to load fallback: {e}")
            self.thesaurus = {}
            self.reverse_index = {}
            self.initialized = True
    
    def get_synonyms(self, word: str, max_results: int = 10) -> List[str]:
        """Get synonyms with error handling"""
        try:
            return super().get_synonyms(word, max_results)
        except Exception as e:
            self.error_log.append({
                'timestamp': time.time(),
                'method': 'get_synonyms',
                'word': word,
                'error': str(e)
            })
            return []  # Return empty list on error
    
    def health_check(self) -> Dict[str, any]:
        """Check the health of the thesaurus system"""
        return {
            'initialized': self.initialized,
            'total_words': len(self.thesaurus),
            'total_reverse_entries': len(self.reverse_index),
            'error_count': len(self.error_log),
            'recent_errors': self.error_log[-5:],
            'cache_exists': self.downloader.processed_file.exists(),
            'raw_file_exists': self.downloader.raw_file.exists()
        }