"""
Maintenance scripts for Moby Thesaurus integration
"""

import json
import os
from pathlib import Path
from .moby_thesaurus import MobyThesaurusDownloader, MobyThesaurusProcessor, RobustMobyThesaurus
import logging

logger = logging.getLogger(__name__)


def update_thesaurus(force_download: bool = False) -> bool:
    """Update thesaurus data"""
    try:
        thesaurus = MobyThesaurusDownloader()
        
        # Check if update needed
        if should_update() or force_download:
            logger.info("Updating thesaurus...")
            if thesaurus.download_thesaurus(force=force_download):
                processor = MobyThesaurusProcessor(thesaurus)
                processor.process_raw_file()
                processor.save_processed_data()
                
                logger.info("Update complete!")
                return True
            else:
                logger.error("Failed to download thesaurus")
                return False
        else:
            logger.info("Thesaurus is up to date")
            return True
    except Exception as e:
        logger.error(f"Error updating thesaurus: {e}")
        return False


def should_update() -> bool:
    """Check if thesaurus should be updated"""
    data_dir = Path("data/thesaurus")
    processed_file = data_dir / "moby-thesaurus-processed.pkl"
    
    # Update if processed file doesn't exist
    if not processed_file.exists():
        return True
    
    # Update if file is older than 30 days
    import time
    file_age = time.time() - processed_file.stat().st_mtime
    return file_age > (30 * 24 * 60 * 60)  # 30 days in seconds


def create_fallback():
    """Create a minimal fallback file for emergency use"""
    common_synonyms = {
        # Search-related terms
        'search': ['find', 'look', 'seek', 'query', 'explore', 'hunt'],
        'find': ['locate', 'discover', 'uncover', 'detect', 'spot'],
        'analyze': ['examine', 'study', 'evaluate', 'assess', 'review'],
        'create': ['make', 'build', 'generate', 'produce', 'develop'],
        'delete': ['remove', 'erase', 'clear', 'eliminate', 'destroy'],
        'update': ['modify', 'change', 'revise', 'edit', 'alter'],
        
        # Programming terms
        'code': ['program', 'script', 'software', 'application'],
        'debug': ['troubleshoot', 'fix', 'repair', 'solve'],
        'error': ['bug', 'problem', 'issue', 'fault', 'mistake'],
        'function': ['method', 'procedure', 'routine', 'operation'],
        'variable': ['parameter', 'value', 'data', 'field'],
        'class': ['object', 'type', 'structure', 'entity'],
        'algorithm': ['procedure', 'method', 'process', 'technique'],
        'data': ['information', 'content', 'details', 'facts'],
        'structure': ['format', 'organization', 'arrangement', 'layout'],
        'system': ['framework', 'platform', 'environment', 'setup'],
        'process': ['procedure', 'operation', 'workflow', 'method'],
        
        # File and document terms
        'file': ['document', 'record', 'item', 'entry'],
        'document': ['paper', 'report', 'text', 'file'],
        'text': ['content', 'writing', 'material', 'information'],
        'image': ['picture', 'photo', 'graphic', 'visual'],
        'video': ['movie', 'clip', 'recording', 'footage'],
        'audio': ['sound', 'recording', 'music', 'voice'],
        
        # User and admin terms
        'user': ['person', 'individual', 'operator', 'client'],
        'admin': ['administrator', 'manager', 'supervisor', 'controller'],
        'setting': ['configuration', 'option', 'preference', 'parameter'],
        'configuration': ['setup', 'arrangement', 'settings', 'options'],
        'option': ['choice', 'alternative', 'selection', 'preference'],
        
        # Common action words
        'show': ['display', 'present', 'reveal', 'exhibit'],
        'hide': ['conceal', 'mask', 'cover', 'obscure'],
        'open': ['access', 'launch', 'start', 'begin'],
        'close': ['shut', 'end', 'finish', 'terminate'],
        'save': ['store', 'preserve', 'keep', 'maintain'],
        'load': ['open', 'retrieve', 'fetch', 'import'],
        'export': ['save', 'output', 'extract', 'transfer'],
        'import': ['load', 'input', 'bring', 'include'],
        
        # Quality and performance terms
        'improve': ['enhance', 'better', 'upgrade', 'optimize'],
        'optimize': ['improve', 'enhance', 'tune', 'refine'],
        'performance': ['speed', 'efficiency', 'capability', 'effectiveness'],
        'quality': ['standard', 'grade', 'level', 'excellence'],
        'fast': ['quick', 'rapid', 'speedy', 'swift'],
        'slow': ['sluggish', 'delayed', 'gradual', 'leisurely'],
        'efficient': ['effective', 'productive', 'optimal', 'streamlined'],
        'accurate': ['precise', 'exact', 'correct', 'true'],
        
        # Common modifiers
        'big': ['large', 'huge', 'massive', 'enormous'],
        'small': ['tiny', 'little', 'mini', 'compact'],
        'new': ['recent', 'fresh', 'modern', 'latest'],
        'old': ['ancient', 'vintage', 'outdated', 'legacy'],
        'good': ['excellent', 'great', 'fine', 'superior'],
        'bad': ['poor', 'terrible', 'awful', 'inferior'],
        'easy': ['simple', 'straightforward', 'effortless', 'basic'],
        'hard': ['difficult', 'challenging', 'complex', 'tough'],
        'complete': ['finished', 'done', 'full', 'total'],
        'incomplete': ['partial', 'unfinished', 'lacking', 'missing']
    }
    
    # Create reverse index for fallback
    reverse_index = {}
    for root_word, synonyms in common_synonyms.items():
        for synonym in synonyms:
            if synonym not in reverse_index:
                reverse_index[synonym] = []
            reverse_index[synonym].append(root_word)
    
    fallback_data = {
        'thesaurus': common_synonyms,
        'reverse_index': reverse_index,
        'version': 'fallback-1.0',
        'created_at': '2025-01-04',
        'description': 'Emergency fallback thesaurus with common programming and search terms'
    }
    
    fallback_path = Path('data/thesaurus/emergency_fallback.json')
    fallback_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(fallback_path, 'w') as f:
        json.dump(fallback_data, f, indent=2)
    
    logger.info(f"Created fallback thesaurus with {len(common_synonyms)} root words at {fallback_path}")
    return True


def health_check_thesaurus() -> dict:
    """Perform a comprehensive health check of the thesaurus system"""
    try:
        thesaurus = RobustMobyThesaurus(
            fallback_file="data/thesaurus/emergency_fallback.json"
        )
        
        # Try to initialize
        thesaurus.initialize(max_retries=1)
        
        # Get health info
        health = thesaurus.health_check()
        
        # Test with sample words
        test_words = ['search', 'code', 'debug', 'create', 'analyze']
        test_results = {}
        
        for word in test_words:
            synonyms = thesaurus.get_synonyms(word, max_results=3)
            test_results[word] = {
                'synonyms_found': len(synonyms),
                'synonyms': synonyms
            }
        
        health['test_results'] = test_results
        health['system_status'] = 'healthy' if health['initialized'] else 'unhealthy'
        
        return health
    
    except Exception as e:
        return {
            'system_status': 'error',
            'error': str(e),
            'initialized': False
        }


def repair_thesaurus() -> bool:
    """Attempt to repair a corrupted thesaurus installation"""
    try:
        logger.info("Attempting to repair thesaurus...")
        
        # Remove corrupted files
        data_dir = Path("data/thesaurus")
        if data_dir.exists():
            for file in data_dir.glob("*.pkl"):
                file.unlink()
            for file in data_dir.glob("*.json"):
                if 'fallback' not in file.name:
                    file.unlink()
        
        # Re-download and process
        return update_thesaurus(force_download=True)
    
    except Exception as e:
        logger.error(f"Repair failed: {e}")
        return False


def get_thesaurus_stats() -> dict:
    """Get comprehensive statistics about the thesaurus"""
    try:
        thesaurus = RobustMobyThesaurus()
        thesaurus.initialize()
        
        if not thesaurus.initialized:
            return {'error': 'Thesaurus not initialized'}
        
        total_words = len(thesaurus.thesaurus)
        total_synonyms = sum(len(synonyms) for synonyms in thesaurus.thesaurus.values())
        avg_synonyms = total_synonyms / total_words if total_words > 0 else 0
        
        # Find word with most synonyms
        max_synonyms = 0
        word_with_most = None
        for word, synonyms in thesaurus.thesaurus.items():
            if len(synonyms) > max_synonyms:
                max_synonyms = len(synonyms)
                word_with_most = word
        
        return {
            'total_root_words': total_words,
            'total_synonyms': total_synonyms,
            'average_synonyms_per_word': round(avg_synonyms, 2),
            'max_synonyms': max_synonyms,
            'word_with_most_synonyms': word_with_most,
            'reverse_index_entries': len(thesaurus.reverse_index),
            'data_size_mb': _get_data_size_mb()
        }
    
    except Exception as e:
        return {'error': str(e)}


def _get_data_size_mb() -> float:
    """Get total size of thesaurus data files in MB"""
    data_dir = Path("data/thesaurus")
    if not data_dir.exists():
        return 0.0
    
    total_size = sum(f.stat().st_size for f in data_dir.glob("*") if f.is_file())
    return round(total_size / (1024 * 1024), 2)


if __name__ == "__main__":
    # Command line interface for maintenance
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python thesaurus_maintenance.py <command>")
        print("Commands: update, fallback, health, repair, stats")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "update":
        force = "--force" in sys.argv
        success = update_thesaurus(force_download=force)
        print("Update successful!" if success else "Update failed!")
    
    elif command == "fallback":
        success = create_fallback()
        print("Fallback created!" if success else "Fallback creation failed!")
    
    elif command == "health":
        health = health_check_thesaurus()
        print(json.dumps(health, indent=2))
    
    elif command == "repair":
        success = repair_thesaurus()
        print("Repair successful!" if success else "Repair failed!")
    
    elif command == "stats":
        stats = get_thesaurus_stats()
        print(json.dumps(stats, indent=2))
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)