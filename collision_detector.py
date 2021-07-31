from pygame import Rect

class CollisionDetector:

    def detect(self, rect, *objects):

        for obj in objects:
            if Rect.colliderect(rect, obj):
                return True
        
        return False
