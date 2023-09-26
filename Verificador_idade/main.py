import wx
import datetime

class HelloFrame(wx.Frame):
    def __init__(self, title):
        #largura, altura
        super().__init__(None, title=title, size=(450, 300))
        self.name = "<unknown>"
        
        vertical_box_sizer = wx.BoxSizer(wx.VERTICAL)
        
        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.Colour(0,100,100))
        vertical_box_sizer.Add(panel, wx.ID_ANY, wx.EXPAND, 10) #Expande a margem da tela.
        
        panel_sizer = wx.BoxSizer(wx.VERTICAL) #Adiciona um boxSizer ao painel.

        panel.SetSizer(panel_sizer)
        
        #5 linhas, 1 coluna com espaçamento de 2 px para cada lado.
        grid = wx.GridSizer(5, 1, 10, 10)

        #fonte
        self.font = wx.Font( wx.FontInfo(10).Bold())
        #nome
        self.name_label = wx.StaticText(panel, label="Nome:")
        self.name_label.SetForegroundColour(wx.Colour(255,255,255))
        self.name_label.SetFont(self.font)
        self.name_input = wx.TextCtrl(panel, size=(250, -1))
        
        #data de nascimento
        self.dtnascimento_label = wx.StaticText(panel, label="Data de Nascimento (DD/MM/AAAA):")
        self.dtnascimento_label.SetForegroundColour(wx.Colour(255,255,255))
        self.dtnascimento_label.SetFont(self.font)

        self.dtnascimento_input = wx.TextCtrl(panel, size=(250, -1))

        #Botão Enviar
        enter_button = wx.Button(panel, label="Enviar", size=(100, -1))
        enter_button.SetBackgroundColour(wx.Colour(0,200,200))
    
        
        #Configurando eventos
        self.Bind(wx.EVT_BUTTON, self.show_message, enter_button)

        

        #Adiciona os elementos na grid.
        grid.AddMany([self.name_label, self.name_input, self.dtnascimento_label, self.dtnascimento_input, enter_button])
        panel_sizer.Add((30,30),0) #Adiciona um espaço vazio no topo
        panel_sizer.Add(grid) #Adiciona a grid no BoxSizer
        panel_sizer.Add((30, 30),0) #adiciona um espaço vazio na parte inferior
        
        self.Centre()

    def calcular_idade(self):

        try:
            #pega os dados do campo de texto data
            birth = self.dtnascimento_input.GetValue()
            #data atual
            date = datetime.datetime.now()
            #ano atual
            ano = ano = int(date.strftime("%Y"))
            #separando a data de nascimento e adicionando numa lista
            dataCortada = birth.split("/")
            #ano de nascimento
            anoNascimento = int(dataCortada[2])
            #retorna a diferença do ano
            return ano - anoNascimento
        
        except:
            dlg = wx.MessageDialog(self, "Você digitou algo inválido, tente novamente", "Erro")
            dlg.ShowModal()
            dlg.Destroy()
        
        
    

    def show_message(self, e):
        birth = self.calcular_idade()

        self.name = self.name_input.GetValue()
        if int(birth) >= 18:
            message = wx.StaticText(self, -1, label=f"Olá {self.name}, você tem {birth} anos. Você já é maior de idade!", pos=(5, 230))
            
        else:
            message = wx.StaticText(self, -1, label=f"Olá {self.name}, você tem {birth} anos. Você ainda é menor de idade!", pos=(5, 230))
        message.SetForegroundColour("white")
        message.SetFont(self.font)
        message.SetBackgroundColour(wx.Colour(0,100,100))
   
        
        
        
class MainApp(wx.App):
    def OnInit(self):
        frame = HelloFrame(title='Validação de Maior Idade')
        frame.Show()
        return True

    def OnExit(self):
        print("Até Mais...")
        return True


app = MainApp()
app.MainLoop()
