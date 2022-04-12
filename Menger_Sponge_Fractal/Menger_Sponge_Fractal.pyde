from Box import Box

a = 0.0;
b = Box(0, 0, 0);
sponge = list();

def setup():
    size(500, 500, P3D);
    sponge.append(b);

def mousePressed():
    global sponge
    next = list();
    for idx in range(len(sponge)):
        newBoxes = sponge[idx].generate();
        next.extend(newBoxes);
    sponge = next;

def draw():
    global a
    background(51);
    stroke(255);
    noFill();
    lights();
    translate(width/2, height/2);
    rotateX(a);
    rotateY(a*0.4);
    rotateZ(a*0.15);
    
    for i in range(len(sponge)):
        sponge[i].show();
    
    a += 0.01;
