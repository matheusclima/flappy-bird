from pygame import Rect

class CollisionDetector:

    def detect(self, rect, *objects):
        for obj in objects:
            if Rect.colliderect(rect, obj):
                print(rect)
                print('-------')  
                print(obj, obj.rect) 
                return True
        
        return False
            

