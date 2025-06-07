import json
import os
from pathlib import Path
from typing import Any, Dict

class SettingsManager:
    """Manages application settings with persistent storage"""
    
    def __init__(self, settings_file: str = "knowledgebase/settings.json"):
        self.settings_file = Path(settings_file)
        self.settings_file.parent.mkdir(parents=True, exist_ok=True)
        self.default_settings = {
            # Display settings
            'theme': 'Dark',
            'items_per_page': 20,
            'show_previews': True,
            
            # Content management
            'auto_save': True,
            'default_category': 'Programming',
            
            # YouTube settings
            'youtube_language': 'en',
            'export_format': 'Markdown',
            
            # Privacy & Analytics
            # NOTE: This feature is currently a placeholder for future analytics implementation
            # When implemented, it would track usage patterns to improve the application
            # All data would be stored locally and never shared with third parties
            'enable_analytics': True,
            
            # LLM settings
            'llm_provider': 'ollama',
            'ollama_api_url': 'http://localhost:11434/api/generate',
            'ollama_model': 'llama3.1:8b',
            'openai_api_key': '',
            'openai_model': 'gpt-3.5-turbo',
            'lmstudio_api_url': 'http://localhost:1234',
            'lmstudio_model': 'granite-3.0-2b-instruct',
            
            # Chat settings
            'chat_use_knowledge_base': True,
            'chat_selected_categories': [],
            'chat_max_context_docs': 5,
            
            # UI preferences
            'sidebar_state': 'expanded',
            'default_view': 'list',  # list or grid
        }
        
    def load_settings(self) -> Dict[str, Any]:
        """Load settings from file, merge with defaults"""
        if self.settings_file.exists():
            try:
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    saved_settings = json.load(f)
                # Merge with defaults to ensure all keys exist
                settings = self.default_settings.copy()
                settings.update(saved_settings)
                return settings
            except Exception as e:
                print(f"Error loading settings: {e}")
        return self.default_settings.copy()
    
    def save_settings(self, settings: Dict[str, Any]) -> bool:
        """Save settings to file"""
        try:
            # Don't save empty API keys
            settings_to_save = settings.copy()
            if not settings_to_save.get('openai_api_key'):
                settings_to_save.pop('openai_api_key', None)
                
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings_to_save, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving settings: {e}")
            return False
    
    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a specific setting value"""
        settings = self.load_settings()
        return settings.get(key, default)
    
    def update_setting(self, key: str, value: Any) -> bool:
        """Update a specific setting"""
        settings = self.load_settings()
        settings[key] = value
        return self.save_settings(settings)
    
    def reset_to_defaults(self) -> bool:
        """Reset all settings to defaults"""
        return self.save_settings(self.default_settings)

# Global settings manager instance
settings_manager = SettingsManager()