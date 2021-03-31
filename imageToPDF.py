from PIL import Image
import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')

layout = [[sg.Image(r'.\imageToPdf\imgtopdf.png')],
        [sg.Text('_' * 80)],
        [sg.Text('Choose A Image', size=(35, 1))],
        [sg.InputText('Image',size=(40,1)), sg.FileBrowse(key='file'), sg.Button('Confirm', key='confirm')],
        [sg.Text('_' * 80)],
        [sg.Text('Amount of Images',size=(30,1))],
        [sg.Text(' ',size=(25,1),key='amountOut')],
        [sg.Text('_'*80)],
        [sg.Text('PDF Name',),sg.Input(size=(25,1),key='name')],
        [sg.Text(' ',size=(80,6))],
        [sg.Button('Submit',size=(25,1),button_color=(1, '#30b1ff'),key='done'), sg.Button('QUIT',size=(25,1),button_color=(1,'red'),key='quit')]
]

window = sg.Window('Image To PDF' ,layout, size=(440, 530))

imgs = []#path
imgDone = []#after image.open
img = [] #list to pdf
cont = 0
while True:
    event, values = window.read()
    file = values['file']
    filename = values['name']
    if event == 'confirm':
        imgs.append(file)
        imgDone.append(Image.open(imgs[cont]))
        img.append(imgDone[cont].convert('RGB'))
        window['amountOut'].update(cont+1)
        cont+=1

    if event == 'done':
        img1 = img[0]
        img.pop(0)
        img1.save(filename+'.pdf',save_all=True,append_images=img)

        '''
        for i in imgs:
            imgDone.append(Image.open(i))

        for n in range (len(imgDone)):
            img.append(imgDone[n].convert('RGB'))'''



    if event == sg.WIN_CLOSED or event == 'quit':
        
        break

