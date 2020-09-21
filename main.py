import copy
from PIL import Image, ImageDraw  # Подключим необходимые библиотеки.
import math

class piramid:
    def __init__(self, image, sh):
        self.maxim = []
        self.minim = []
        self.sred = []
        self.porog = [[0]]

        self._create_piramid(image)
        self.obhod(sh)


    def set_maxim(self, maxim):
        self.maxim = copy.deepcopy(maxim)

    def set_minim(self, minim):
        self.minim = copy.deepcopy(minim)

    def set_sred(self, sred):
        self.sred = copy.deepcopy(sred)

    def get_maxim(self):
        return self.maxim

    def get_minim(self):
        return self.minim

    def get_sr(self):
        return self.sred

    def get_znach(self, image):
        new_mas_max = [[0 for j in range(len(image[0]) // 2)] for i in range(len(image) // 2)]
        new_mas_min = [[0 for j in range(len(image[0]) // 2)] for i in range(len(image) // 2)]
        new_mas_sr = [[0 for j in range(len(image[0]) // 2)] for i in range(len(image) // 2)]

        for i in range(0, len(new_mas_min)):
            for j in range(0, len(new_mas_min[0])):
                new_mas_max[i][j] = max(image[i * 2][j * 2], image[i * 2 + 1][j * 2],
                                        image[i * 2][j * 2 + 1], image[i * 2 + 1][j * 2 + 1])
                new_mas_min[i][j] = min(image[i * 2][j * 2], image[i * 2 + 1][j * 2],
                                        image[i * 2][j * 2 + 1], image[i * 2 + 1][j * 2 + 1])
                new_mas_sr[i][j] = (image[i * 2][j * 2] + image[i * 2 + 1][j * 2] +
                                    image[i * 2][j * 2 + 1] + image[i * 2 + 1][j * 2 + 1]) / 4
        if len(image[0]) % 2 != 0:
            n = len(image) // 2
            for i in range(n):
                new_mas_max[i].append(max(image[i * 2][-1], image[i * 2 + 1][-1]))
                new_mas_min[i].append(min(image[i * 2][-1], image[i * 2 + 1][-1]))
                new_mas_sr[i].append((image[i * 2][-1] + image[i * 2 + 1][-1]) / 2)
        if len(image) % 2 != 0:
            n = len(image[0]) // 2
            new_str_max = []
            new_str_min = []
            new_str_sr = []
            for i in range(n):
                new_str_max.append(max(image[-1][i * 2], image[-1][i * 2 + 1]))
                new_str_min.append(min(image[-1][i * 2], image[-1][i * 2 + 1]))
                new_str_sr.append((image[-1][i * 2] + image[-1][i * 2 + 1]) / 2)
            new_mas_max.append(new_str_max)
            new_mas_sr.append(new_str_sr)
            new_mas_min.append(new_str_min)
        if len(image) % 2 != 0 and len(image[0]) % 2 != 0:
            new_mas_min[-1].append(image[-1][-1])
            new_mas_max[-1].append(image[-1][-1])
            new_mas_sr[-1].append(image[-1][-1])
        return new_mas_min, new_mas_sr, new_mas_max

    def get_min_znach(self, image):
        new_mas_min = [[0 for j in range(len(image[0]) // 2)] for i in range(len(image) // 2)]

        for i in range(0, len(new_mas_min)):
            for j in range(0, len(new_mas_min[0])):

                new_mas_min[i][j] = min(image[i * 2][j * 2], image[i * 2 + 1][j * 2],
                                        image[i * 2][j * 2 + 1], image[i * 2 + 1][j * 2 + 1])

        if len(image[0]) % 2 != 0:
            n = len(image) // 2
            for i in range(n):
                new_mas_min[i].append(min(image[i * 2][-1], image[i * 2 + 1][-1]))

        if len(image) % 2 != 0:
            n = len(image[0]) // 2
            new_str_min = []
            for i in range(n):
                new_str_min.append(min(image[-1][i * 2], image[-1][i * 2 + 1]))

            new_mas_min.append(new_str_min)
        if len(image) % 2 != 0 and len(image[0]) % 2 != 0:
            new_mas_min[-1].append(image[-1][-1])
        return new_mas_min

    def get_max_znach(self, image):
        new_mas_max = [[0 for j in range(len(image[0]) // 2)] for i in range(len(image) // 2)]

        for i in range(0, len(new_mas_max)):
            for j in range(0, len(new_mas_max[0])):
                new_mas_max[i][j] = max(image[i * 2][j * 2], image[i * 2 + 1][j * 2],
                                        image[i * 2][j * 2 + 1], image[i * 2 + 1][j * 2 + 1])

        if len(image[0]) % 2 != 0:
            n = len(image) // 2
            for i in range(n):
                new_mas_max[i].append(max(image[i * 2][-1], image[i * 2 + 1][-1]))

        if len(image) % 2 != 0:
            n = len(image[0]) // 2
            new_str_max = []
            for i in range(n):
                new_str_max.append(max(image[-1][i * 2], image[-1][i * 2 + 1]))

            new_mas_max.append(new_str_max)

        if len(image) % 2 != 0 and len(image[0]) % 2 != 0:

            new_mas_max[-1].append(image[-1][-1])

        return new_mas_max

    def get_sr_znach(self, image):
        new_mas_sr = [[0 for j in range(len(image[0]) // 2)] for i in range(len(image) // 2)]

        for i in range(0, len(new_mas_sr)):
            for j in range(0, len(new_mas_sr[0])):
                new_mas_sr[i][j] = (image[i * 2][j * 2] + image[i * 2 + 1][j * 2] +
                                    image[i * 2][j * 2 + 1] + image[i * 2 + 1][j * 2 + 1]) // 4
        if len(image[0]) % 2 != 0:
            n = len(image) // 2
            for i in range(n):
                new_mas_sr[i].append((image[i * 2][-1] + image[i * 2 + 1][-1]) // 2)
        if len(image) % 2 != 0:
            n = len(image[0]) // 2
            new_str_sr = []
            for i in range(n):
                new_str_sr.append((image[-1][i * 2] + image[-1][i * 2 + 1]) // 2)
            new_mas_sr.append(new_str_sr)
        if len(image) % 2 != 0 and len(image[0]) % 2 != 0:

            new_mas_sr[-1].append(image[-1][-1])
        return new_mas_sr

    def _create_piramid(self, image):
        mmin, msr, mmax = self.get_znach(image)

        while True:
            self.minim.append(mmin)
            self.maxim.append(mmax)
            self.sred.append(msr)
            if len(mmin) < 3 or len(mmin[0]) < 3:
                return
            mmin = self.get_min_znach(mmin)
            mmax = self.get_max_znach(mmax)
            msr = self.get_sr_znach(msr)

    def lanc(self, x):
        n = 2
        if abs(x) < 3:
            if x == 0:
                return 1
            else:
                return n * math.sin(math.pi * x) * math.sin(math.pi * x / n) / (math.pi * math.pi * x * x)
        else:
            return 0

    def get_f(self, x, y, x1, y1):
        s = 0
        n_zn_x = 0
        n_zn_y = 0
        k_zn_x = len(self.porog)
        k_zn_y = len(self.porog[0])
        n = 2
        if x - n + 1 > 0:
            n_zn_x = x - n + 1
        if y - n + 1 > 0:
            n_zn_y = y - n + 1
        if x + n < len(self.porog):
            k_zn_x = x + n
        if y + n < len(self.porog[0]):
            k_zn_y = y + n
        for i in range(n_zn_x, k_zn_x):
            for j in range(n_zn_y, k_zn_y):
                s += self.porog[i][j][0] * self.lanc(x - i) * self.lanc(y - j)
        return s

    def uvel1(self):
        new_image = [[[0, 0] for i in range(len(self.porog[0]) * 2)] for j in range(len(self.porog) * 2)]
        for i in range(len(self.porog)):
            for j in range(len(self.porog[0])):

                n = 2

                if self.porog[i][j][1] == 1:
                    new_image[i * 2][j * 2][0] = self.porog[i][j][0]
                    new_image[i * 2 + 1][j * 2][0] = self.porog[i][j][0]
                    new_image[i * 2][j * 2 + 1][0] = self.porog[i][j][0]
                    new_image[i * 2 + 1][j * 2 + 1][0] = self.porog[i][j][0]
                    new_image[i * 2][j * 2][1] = self.porog[i][j][1]
                    new_image[i * 2 + 1][j * 2][1] = self.porog[i][j][1]
                    new_image[i * 2][j * 2 + 1][1] = self.porog[i][j][1]
                    new_image[i * 2 + 1][j * 2 + 1][1] = self.porog[i][j][1]


                else:
                    new_image[i * 2][j * 2][0] = self.get_f(i, j, i * 2, j * 2)
                    new_image[i * 2 + 1][j * 2][0] = self.get_f(i, j, i * 2 + 1, j * 2)
                    new_image[i * 2][j * 2 + 1][0] = self.get_f(i, j, i * 2, j * 2 + 1)
                    new_image[i * 2 + 1][j * 2 + 1][0] = self.get_f(i, j, i * 2 + 1, j * 2 + 1)
                    new_image[i * 2][j * 2][1] = self.porog[i][j][1]
                    new_image[i * 2 + 1][j * 2][1] = self.porog[i][j][1]
                    new_image[i * 2][j * 2 + 1][1] = self.porog[i][j][1]
                    new_image[i * 2 + 1][j * 2 + 1][1] = self.porog[i][j][1]
        self.porog = new_image

    def uvel2(self):
        new_image = [[[0, 0] for i in range(len(self.porog[0]) * 2)] for j in range(len(self.porog) * 2)]
        for i in range(len(self.porog)):
            for j in range(len(self.porog[0])):

                if self.porog[i][j][1] == 1:
                    new_image[i * 2][j * 2][0] = self.porog[i][j][0]
                    new_image[i * 2 + 1][j * 2][0] = self.porog[i][j][0]
                    new_image[i * 2][j * 2 + 1][0] = self.porog[i][j][0]
                    new_image[i * 2 + 1][j * 2 + 1][0] = self.porog[i][j][0]
                    new_image[i * 2][j * 2][1] = self.porog[i][j][1]
                    new_image[i * 2 + 1][j * 2][1] = self.porog[i][j][1]
                    new_image[i * 2][j * 2 + 1][1] = self.porog[i][j][1]
                    new_image[i * 2 + 1][j * 2 + 1][1] = self.porog[i][j][1]
                else:
                    if i == len(self.porog) - 1:
                        if j == len(self.porog[0]) - 1:
                            new_image[i * 2][j * 2][0] = self.porog[i][j][0]
                            new_image[i * 2 + 1][j * 2][0] = self.porog[i][j][0]
                            new_image[i * 2][j * 2 + 1][0] = self.porog[i][j][0]
                            new_image[i * 2 + 1][j * 2 + 1][0] = self.porog[i][j][0]
                            new_image[i * 2][j * 2][1] = self.porog[i][j][1]
                            new_image[i * 2 + 1][j * 2][1] = self.porog[i][j][1]
                            new_image[i * 2][j * 2 + 1][1] = self.porog[i][j][1]
                            new_image[i * 2 + 1][j * 2 + 1][1] = self.porog[i][j][1]
                        else:
                            new_image[i * 2][j * 2][0] = self.porog[i][j][0]
                            new_image[i * 2 + 1][j * 2][0] = self.porog[i][j][0]
                            new_image[i * 2][j * 2 + 1][0] = (self.porog[i][j][0] + self.porog[i][j + 1][0]) / 2
                            new_image[i * 2 + 1][j * 2 + 1][0] = (self.porog[i][j][0] + self.porog[i][j + 1][0]) / 2
                            new_image[i * 2][j * 2][1] = self.porog[i][j][1]
                            new_image[i * 2 + 1][j * 2][1] = self.porog[i][j][1]
                            new_image[i * 2][j * 2 + 1][1] = self.porog[i][j][1]
                            new_image[i * 2 + 1][j * 2 + 1][1] = self.porog[i][j][1]
                    elif j == len(self.porog[0]) - 1:
                        new_image[i * 2][j * 2][0] = self.porog[i][j][0]
                        new_image[i * 2 + 1][j * 2][0] = (self.porog[i][j][0] + self.porog[i + 1][j][0]) / 2
                        new_image[i * 2][j * 2 + 1][0] = (self.porog[i][j][0])
                        new_image[i * 2 + 1][j * 2 + 1][0] = (self.porog[i][j][0] + self.porog[i + 1][j][0]) / 2
                        new_image[i * 2][j * 2][1] = self.porog[i][j][1]
                        new_image[i * 2 + 1][j * 2][1] = self.porog[i][j][1]
                        new_image[i * 2][j * 2 + 1][1] = self.porog[i][j][1]
                        new_image[i * 2 + 1][j * 2 + 1][1] = self.porog[i][j][1]
                    else:
                        new_image[i * 2][j * 2][0] = self.porog[i][j][0]
                        new_image[i * 2 + 1][j * 2][0] = (self.porog[i][j][0] + self.porog[i + 1][j][0]) / 2
                        new_image[i * 2][j * 2 + 1][0] = (self.porog[i][j][0] + self.porog[i][j + 1][0]) / 2
                        new_image[i * 2 + 1][j * 2 + 1][0] = (self.porog[i][j][0] + self.porog[i + 1][j][0] + self.porog[i][j + 1][0] + self.porog[i + 1][j + 1][0]) / 4
                        new_image[i * 2][j * 2][1] = self.porog[i][j][1]
                        new_image[i * 2 + 1][j * 2][1] = self.porog[i][j][1]
                        new_image[i * 2][j * 2 + 1][1] = self.porog[i][j][1]
                        new_image[i * 2 + 1][j * 2 + 1][1] = self.porog[i][j][1]
        self.porog = new_image

    def obhod(self, sh):
        self.porog = [[[0, 0] for i in range(len(self.maxim[-1][0]))] for j in range(len(self.maxim[-1]))]
        minim = self.minim[-1]
        maxim = self.maxim[-1]
        sred = self.sred[-1]

        for i in range(len(maxim)):
            for j in range(len(maxim[0])):
                self.porog[i][j][0] = sred[i][j]#(maxim[i][j] + minim[i][j] + sred[i][j]) / 3#((maxim[i][j] + minim[i][j]) / 2 + sred[i][j]) / 2
        k = len(self.maxim) - 2

        while k >= 6:
            self.uvel2()
            minim = self.minim[k]
            maxim = self.maxim[k]
            sred = self.sred[k]

            for i in range(len(maxim)):
                for j in range(len(maxim[0])):
                    if self.porog[i][j][1] != 1:
                        if maxim[i][j] - minim[i][j] > 3 * sh:
                            self.porog[i][j][0] = sred[i][j]#(maxim[i][j] + minim[i][j] + sred[i][j]) / 3#((maxim[i][j] + minim[i][j]) / 2 + sred[i][j]) / 2
                        else:
                            self.porog[i][j][1] = 1
                            #print(k)
            k -= 1

    def kost(self):
        new_mas = [[0 for i in range(len(self.porog[0]))] for j in range(len(self.porog))]
        for i in range(len(self.porog)):
            for j in range(len(self.porog)):
                new_mas[i][j] = self.porog[i][j][0]
        return new_mas

    def binar(self, image):

        new_image = [[0 for i in range(len(image[0]))] for j in range(len(image))]
        ch_pix = 128
        for i in range(len(new_image) // ch_pix):
            for j in range(len(new_image[0]) // ch_pix):
                for k in range(ch_pix):
                    for t in range(ch_pix):
                        if image[i * ch_pix + k][j * ch_pix + t] > self.porog[i][j][0]:
                            new_image[i * ch_pix + k][j * ch_pix + t] = 255

        for i in range(len(new_image) % ch_pix):
            for j in range(len(new_image[0]) % ch_pix):
                print(image[(len(new_image) // ch_pix) * ch_pix + i][(len(new_image[0]) // ch_pix) * ch_pix + j], self.porog[len(new_image) // ch_pix][len(new_image[0]) // ch_pix][0])
                if image[(len(new_image) // ch_pix) * ch_pix + i][(len(new_image[0]) // ch_pix) * ch_pix + j] > self.porog[len(new_image) // ch_pix][len(new_image[0]) // ch_pix][0]:
                    new_image[(len(new_image) // ch_pix) * ch_pix + i][(len(new_image[0]) // ch_pix) * ch_pix + j] = 255

        return new_image


def shum(image):
    sr = [[0 for i in range(len(image[0]) // 32)] for j in range(len(image) // 32)]
    min_disp = 1000000000
    for i in range(len(sr)):
        for j in range(len(sr[0])):
            pr = 0
            for k in range(32):
                for t in range(32):
                    pr += image[i * 32 + k][j * 32 + t]
            sr[i][j] = pr / (32 * 32)
            pr = 0
            for k in range(32):
                for t in range(32):
                    pr += (sr[i][j] - image[i * 32 + k][j * 32 + t]) ** 2
            disp = pr / (32 * 32 - 1)
            if disp < min_disp:
                min_disp = disp
    return min_disp


def shum1(image):
    sr = [[0 for i in range(len(image[0]) // 32)] for j in range(len(image) // 32)]
    min_disp = 1000000000
    mas_disp = [[1000000000, 0, 0], [1000000000, 0, 0], [1000000000, 0, 0], [1000000000, 0, 0], [1000000000, 0, 0], [1000000000, 0, 0], [1000000000, 0, 0], [1000000000, 0, 0], [1000000000, 0, 0], [1000000000, 0, 0]]
    max_min_disp = 0
    for i in range(len(sr)):
        for j in range(len(sr[0])):
            pr = 0
            for k in range(32):
                for t in range(32):
                    pr += image[i * 32 + k][j * 32 + t]
            sr[i][j] = pr / (32 * 32)
            pr = 0
            for k in range(32):
                for t in range(32):
                    pr += (sr[i][j] - image[i * 32 + k][j * 32 + t]) ** 2
            disp = pr / (32 * 32 - 1)
            for e in mas_disp:
                if e[0] > disp and sr[i][j] < 200 and sr[i][j] > 50:
                    mas_disp.remove(e)
                    mas_disp.append([disp, i, j])
                    break
            #if disp < min_disp and sr[i][j] < 155 and sr[i][j] > 100:
    razn = 10000000
    for i in mas_disp:
        if abs(i[1] - i[2]) < razn:
            razn = abs(i[1] - i[2])
            min_disp = i[0]
    return min_disp


def read_image(name):
    image = Image.open(name)  # Открываем изображение.

    pix = image.load()  # Выгружаем значения пикселей.
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.

    new_mas = [[0 for i in range(width)] for j in range(height)]
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            new_mas[j][i] = S

    return new_mas


def print_image(image1, old_name, name):
    image = Image.open(old_name)  # Открываем изображение.
    draw = ImageDraw.Draw(image)
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    for i in range(len(image1)):
        for j in range(len(image1[0])):
            draw.point((j, i), (int(image1[i][j]), int(image1[i][j]), int(image1[i][j])))
    image.save(name, "TIFF")
    del draw


for i in range(1, 10):
    print(i)
    a = 'D:\обработка изображений\dz3\TestSet1\\000' + str(i) + '.jpg'
    mas = read_image(a)
    sh1 = shum1(mas)
    sh2 = shum(mas)
    res = piramid(mas, sh2)
    res1 = res.binar(mas)
    print_image(res1, a, 'D:\обработка изображений\dz3\TestSet1\qw\\' + 'b1' + str(i) + '.tiff')
