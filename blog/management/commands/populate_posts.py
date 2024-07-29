from typing import Any
from blog.models import Post,Category
import random 

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command inserts post data"
    
    def handle(self, *args: Any, **options: Any):
        #Deleting existing data
        Post.objects.all().delete()
        
        titles = ["Whispers of the Forgotten Realm", "The Enchanted Voyage", "Mysteries of the Midnight Garden", "Echoes of the Lost City", "Chronicls of the Shadow War",
          "Secrets Beneath the Silver Moon", "The Last Dragon's Cry", "Legends of the Ancient Forest", "Guardians of the Hidden Temple",
          "The Phantom's Whisper""Songs of the Eternal Stars", "The Wishing Well of Dreams", "Beneath the Veil of Shadows", "Dance of the Mystic Flames",
          "Tales from the Crystal Cavern", "The Guardian's Oath", "Journey to the Forgotten Isle", "The Clockwork Enigma", "Moonlit Serenade", "The Alchemist's Secret"]

        contents = ['In the ancient lands where time stands still, the Whispers of the Forgotten Realm echo through the winds, telling tales of lost civilizations and untold secrets.',
                    'Embark on The Enchanted Voyage, where brave adventurers set sail across mystical seas, discovering hidden treasures and encountering mythical creatures.',
                    'Under the cloak of darkness, the Mysteries of the Midnight Garden unfold, revealing enchanted flora, hidden pathways, and secrets whispered by the night.',
                    'In the heart of the jungle, the Echoes of the Lost City call out, inviting explorers to uncover its buried secrets and ancient wisdom.',
                    'As the battle between light and shadow rages on, the Chronicles of the Shadow War recount heroic deeds, fierce conflicts, and the relentless struggle for power.',
                    'Beneath the glow of the silver moon, the Secrets Beneath the Silver Moon are unveiled, illuminating hidden truths and magical wonders.',
                    'With a roar that shakes the heavens, The Last Dragons Cry signals the end of an era and the beginning of a new legend, filled with bravery and sacrifice.',
                    'Deep within the ancient woods, the Legends of the Ancient Forest come alive, telling stories of mythical beings, enchanted groves, and timeless magic.',
                    'In the depths of a forgotten temple, the Guardians of the Hidden Temple stand watch, protecting sacred relics and ancient knowledge from those who seek to exploit them.',
                    'In the silent night, The Phantoms Whisper carries messages from the beyond, guiding the living with cryptic warnings and mysterious prophecies.',
                    'In the vast cosmos, the Songs of the Eternal Stars sing of ancient legends, celestial wonders, and the infinite mysteries of the universe.',
                    'At the heart of a magical glen, the Wishing Well of Dreams grants the deepest desires of those pure of heart, weaving their wishes into reality.',
                    'Hidden within the shadows, Beneath the Veil of Shadows lies a realm of intrigue and mystery, where secrets are guarded and destinies are forged.',
                    'In the heart of the enchanted forest, the Dance of the Mystic Flames mesmerizes all who witness it, revealing the magic and power of the elemental spirits.',
                    'Deep underground, the Tales from the Crystal Cavern tell of forgotten civilizations, sparkling treasures, and the echoes of ancient magic.',
                    'Bound by honor, the Guardians Oath is a sacred promise to protect the realm from darkness, upheld by warriors of unmatched courage and strength.',
                    'Across the vast ocean, the Journey to the Forgotten Isle takes adventurers to a place where time stands still and untold treasures await discovery.',
                    'Within the gears and cogs, the Clockwork Enigma puzzles the greatest minds, holding the key to unlocking the secrets of time and innovation.',
                    'Under the moons gentle glow, the Moonlit Serenade enchants the night, weaving melodies of love, longing, and the beauty of the nocturnal world.',
                    'In a hidden laboratory, The Alchemists Secret unveils the mysteries of transmutation, eternal life, and the pursuit of ultimate knowledge.']

        img_urls = ["https://picsum.photos/id/1/800/400",
            "https://picsum.photos/id/2/800/400",
            "https://picsum.photos/id/3/800/400",
            "https://picsum.photos/id/4/800/400",
            "https://picsum.photos/id/5/800/400",
            "https://picsum.photos/id/6/800/400",
            "https://picsum.photos/id/7/800/400",
            "https://picsum.photos/id/8/800/400",
            "https://picsum.photos/id/9/800/400",
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/11/800/400",
            "https://picsum.photos/id/12/800/400",
            "https://picsum.photos/id/13/800/400",
            "https://picsum.photos/id/14/800/400",
            "https://picsum.photos/id/15/800/400",
            "https://picsum.photos/id/16/800/400",
            "https://picsum.photos/id/17/800/400",
            "https://picsum.photos/id/18/800/400",
            "https://picsum.photos/id/19/800/400",
            "https://picsum.photos/id/20/800/400"]

        
        categories = Category.objects.all()
        for title, content, img_url in (zip(titles,contents,img_urls)):
            category = random.choice(categories)
            Post.objects.create(title=title,content=content,img_url=img_url,category = category)

        self.stdout.write(self.style.SUCCESS("Completed inserting data!"))