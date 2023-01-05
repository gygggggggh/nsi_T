from PIL import Image
# changer la luminosité de l'image
im = Image.open("python/PIL/index.jpg")
longueur, largeur = im.size

im_lum = Image.new("RGB", (longueur, largeur))

pixels_im = im.load()
pixels_im_lum = im_lum.load()

delta_lum = -80

for y in range(largeur):
    for x in range(longueur):
        p = pixels_im[x, y]
        r = p[0] + delta_lum
        v = p[1] + delta_lum
        b = p[2] + delta_lum
        pixels_im_lum[x, y] = (r, v, b)

im_lum.save("python/PIL/index_lum.jpg")

# changer le contraste de l'image

im_contraste = Image.new("RGB", (longueur, largeur))

pixels_im_contraste = im_contraste.load()

delta_contraste = 2

for y in range(largeur):
    for x in range(longueur):
        p = pixels_im[x, y]
        r = int(p[0] * delta_contraste)
        v = int(p[1] * delta_contraste)
        b = int(p[2] * delta_contraste)
        pixels_im_contraste[x, y] = (r, v, b)

im_contraste.save("python/PIL/index_contraste.jpg")

# changer en noir et blanc

im_noir_blanc = Image.new("RGB", (longueur, largeur))

pixels_im_noir_blanc = im_noir_blanc.load()

for y in range(largeur):
    for x in range(longueur):
        p = pixels_im[x, y]
        r = p[0]
        v = p[1]
        b = p[2]
        moy = (r + v + b) // 3
        pixels_im_noir_blanc[x, y] = (moy, moy, moy)

im_noir_blanc.save("python/PIL/index_noir_blanc.jpg")

# changer en noir et blanc avec seuil

im_noir_blanc_seuil = Image.new("RGB", (longueur, largeur))

pixels_im_noir_blanc_seuil = im_noir_blanc_seuil.load()

seuil = 150

for y in range(largeur):
    for x in range(longueur):
        p = pixels_im[x, y]
        r = p[0]
        v = p[1]
        b = p[2]
        moy = (r + v + b) // 3
        if moy > seuil:
            pixels_im_noir_blanc_seuil[x, y] = (255, 255, 255)
        else:
            pixels_im_noir_blanc_seuil[x, y] = (0, 0, 0)

im_noir_blanc_seuil.save("python/PIL/index_noir_blanc_seuil.jpg")

# prend selement une couleur rouge

im_rouge = Image.new("RGB", (longueur, largeur))

pixels_im_rouge = im_rouge.load()


for y in range(largeur):
    for x in range(longueur):
        p = pixels_im[x, y]
        r = p[0]
        v = p[1]
        b = p[2]
        pixels_im_rouge[x, y] = (r, 0, 0)

im_rouge.save("python/PIL/index_rouge.jpg")

# prend selement une couleur verte

im_vert = Image.new("RGB", (longueur, largeur))

pixels_im_vert = im_vert.load()


for y in range(largeur):
    for x in range(longueur):
        p = pixels_im[x, y]
        r = p[0]
        v = p[1]
        b = p[2]
        pixels_im_vert[x, y] = (0, v, 0)

im_vert.save("python/PIL/index_vert.jpg")

# prend selement une couleur bleu

im_bleu = Image.new("RGB", (longueur, largeur))

pixels_im_bleu = im_bleu.load()


for y in range(largeur):
    for x in range(longueur):
        p = pixels_im[x, y]
        r = p[0]
        v = p[1]
        b = p[2]
        pixels_im_bleu[x, y] = (0, 0, b)

im_bleu.save("python/PIL/index_bleu.jpg")

# Rec. 709

im_rec709 = Image.new("RGB", (longueur, largeur))

pixels_im_rec709 = im_rec709.load()

for y in range(largeur):
    for x in range(longueur):
        p = pixels_im[x, y]
        r = p[0]
        v = p[1]
        b = p[2]
        r = int(0.2126 * r + 0.7152 * v + 0.0722 * b)
        v = int(0.2126 * r + 0.7152 * v + 0.0722 * b)
        b = int(0.2126 * r + 0.7152 * v + 0.0722 * b)
        pixels_im_rec709[x, y] = (r, v, b)

im_rec709.save("python/PIL/index_rec709.jpg")




# rotation de l'image sans utiliser la fonction rotate

im_rotation = Image.new("RGB", (largeur, longueur))

pixels_im_rotation = im_rotation.load()

for y in range(largeur):
    for x in range(longueur):
        p = pixels_im[x, y]
        pixels_im_rotation[y, x] = p
        

im_rotation.save("python/PIL/index_rotation.jpg")

# effet relief

im_relief = Image.new("RGB", (longueur, largeur))

pixels_im_relief = im_relief.load()

for y in range(largeur):
    for x in range(longueur):
        if x < longueur - 1 and y < largeur - 1:
            p = pixels_im[x, y]
            p2 = pixels_im[x + 1, y + 1]
            r = p[0] - p2[0] + 128
            v = p[1] - p2[1] + 128
            b = p[2] - p2[2] + 128
            pixels_im_relief[x, y] = (r, v, b)

im_relief.save("python/PIL/index_relief.jpg")

# effet de flou en moyenne des pixels autour

im_flou = Image.new("RGB", (longueur, largeur))

pixels_im_flou = im_flou.load()

for y in range(largeur):
    for x in range(longueur):
        if x > 0 and y > 0 and x < longueur - 1 and y < largeur - 1:
            p = pixels_im[x, y]
            p2 = pixels_im[x + 1, y]
            p3 = pixels_im[x - 1, y]
            p4 = pixels_im[x, y + 1]
            p5 = pixels_im[x, y - 1]
            r = (p[0] + p2[0] + p3[0] + p4[0] + p5[0]) // 5
            v = (p[1] + p2[1] + p3[1] + p4[1] + p5[1]) // 5
            b = (p[2] + p2[2] + p3[2] + p4[2] + p5[2]) // 5
            pixels_im_flou[x, y] = (r, v, b)

im_flou.save("python/PIL/index_flou.jpg")











# show all images


'''
im.show()
im_lum.show()
im_contraste.show()
im_noir_blanc.show()
im_noir_blanc_seuil.show()
im_rouge.show()
im_vert.show()
im_bleu.show()
im_rec709.show()
im_message.show()
im_rotation.show()
im_relief.show()
im_flou.show()

'''


