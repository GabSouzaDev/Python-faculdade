import wx
import datetime

class Birthday(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Happy Birthday", size=(300,300))

        #Pegar a data de hoje e organizar o formato
        date = datetime.datetime.today()
        self.dataTratada = date.strftime("%d/%m/%Y")

        
        
        #criar um painel
        panel = wx.Panel(self)
        #Criar um grid com 4 linhas e 1 colunas com 5px de espaço ao redor de cada celula
        grid = wx.GridSizer(4, 1, 5, 5)
        #fonte grande

        #Campo de nome
        name = wx.StaticText(panel, label="Name:", pos=(5,5))
        self.nameField = wx.TextCtrl(panel, size=(150, -1), pos=(60, 1))
        #Campo de idade
        age = wx.StaticText(panel, label="Birth day:", pos=(5,45))
        self.ageField = wx.TextCtrl(panel, size=(150, -1), pos=(60, 40))

        #botão de entrada
        welcome_button = wx.Button(panel, label="Entrar", pos=(60, 90), size=(150, -1))

        #botão de aniversário
        birthday_button = wx.Button(panel, label="Birthday", pos=(60, 150), size=(150, -1))

        #Configurar o menu
        filemenu = wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&Sobre")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "&Sair")

        #Criar um menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&Arquivos")
        self.SetMenuBar(menuBar)

        #Configurar eventos
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_BUTTON, self.OnEnterButtonClick, welcome_button)
        self.Bind(wx.EVT_BUTTON, self.OnBirthdayButtonClick, birthday_button)

        self.Show(True)

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "Alguma coisa, não faço ideia", "Sobre isso")
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, e):
        self.Close(True)

    def OnEnterButtonClick(self, e):
        saida = self.nameField.GetValue()
        welcome = wx.StaticText(self,-1,f"Welcome {saida} ",(60,130))

    def OnBirthdayButtonClick(self,e):
       val2 = self.ageField.GetValue()
       
       if(val2 == self.dataTratada):
           happy = wx.StaticText(self,-1,"Happy Birthday :)",(60,180))
       else:
           happy = wx.StaticText(self,-1,"Ainda não é seu aniversário :)",(60,180))

class MainApp(wx.App):
    def OnInit(self):
       frame = Birthday()
       frame.Show()
       return True

app = MainApp()
app.MainLoop()
