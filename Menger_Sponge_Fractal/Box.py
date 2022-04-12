class Box:
    def __init__(self, x, y, z, _r=250):
        self.r = 0.0;
        
        self.x = x
        self.y = y
        self.z = z
        self._r = _r
        
        self.pos = PVector(x, y, z);
        self.r = self._r
        
    def generate(self):
        boxes = list()
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    sum = int(abs(i) + abs(j) + abs(k));
                    newR = self.r / 3;
                    if sum > 1:
                        b = self(self.pos.x+i*newR, self.pos.y+j*newR, self.pos.z+k*newR, newR)
                        boxes.append(b)
        return boxes
        
    def show(self):
        pushMatrix();
        translate(self.pos.x, self.pos.y, self.pos.z);
        noStroke();
        fill(166, 125, 18, 255);
        box(self.r);
        popMatrix();
        
    def __call__(self, x, y, z, r):
        return Box(x, y, z, r)
