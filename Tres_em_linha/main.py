#Tic Tac Toe
#objetivos:
# OK Criar um Menu
# OK Quando cada usuario seleciona um botão, você pode definir o rótulo do botão para seu simbolo.
# OK Precisa de 2 verificações após cada jogada para ver se houve vitoria ou empate.
# OK Representação interna da grade para poder determinar quem ganhou.
# OK Adicionar caixa de diálogo para obter os nomes dos jogadores.
import wx

class TicTacFrame(wx.Frame):
    def __init__(self, title):
        super().__init__(parent=None, title=title, size=(300,400))

        #painel grid
        panel = wx.Panel(self)
        grid = wx.GridSizer(4,3,5,5)

       
        

        #caixa de dialogo para obter o nome dos jogadores
        #player 1
        player1Dlg = wx.TextEntryDialog(None, 'Insira seu nome/apelido', 'Registrar jogador 1 - X', 'Jogador 1')
        if player1Dlg.ShowModal() == wx.ID_OK:
            self.player1 = player1Dlg.GetValue()
        player1Dlg.Destroy()
        #player 2
        player2Dlg = wx.TextEntryDialog(None, 'Insira seu nome/apelido', 'Registrar jogador 2 - O', 'Jogador 2')

        if player2Dlg.ShowModal() == wx.ID_OK:
            self.player2 = player2Dlg.GetValue()
        player2Dlg.Destroy()

        #Contador de Rodadas do jogo
        self.round = 0

        #contabilizar a pontuação dos players
        self.player1_score = 0
        self.player2_score = 0
        self.velha_score = 0

        #botões do game
        self.simbolo = ['X', 'O']
        
        self.botao1 = wx.Button(panel, label='', size=(70,70))
        self.botao2 = wx.Button(panel, label='', size=(70,70))
        self.botao3 = wx.Button(panel, label='', size=(70,70))
        self.botao4 = wx.Button(panel, label='', size=(70,70))
        self.botao5 = wx.Button(panel, label='', size=(70,70))
        self.botao6 = wx.Button(panel, label='', size=(70,70))
        self.botao7 = wx.Button(panel, label='', size=(70,70))
        self.botao8 = wx.Button(panel, label='', size=(70,70))
        self.botao9 = wx.Button(panel, label='', size=(70,70))

        #Notificador da vez do jogador
        self.player = wx.StaticText(panel, label=f'{self.player1}, sua vez!')

        #adicionando ao grid
        grid.AddMany([self.botao1, self.botao2, self.botao3, self.botao4, self.botao5, self.botao6, self.botao7, self.botao8, self.botao9, self.player])
        panel.SetSizer(grid)

        #Menu
        filemenu = wx.Menu()
        menuScore = filemenu.Append(wx.ID_ANY, '&Pontuação')
        filemenu.AppendSeparator()
        menuRules = filemenu.Append(wx.ID_OK, '&Regras')
        filemenu.AppendSeparator()
        menuAbout = filemenu.Append(wx.ID_ABOUT, '&Sobre')
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "&Sair")

        #Menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&Menu")
        self.SetMenuBar(menuBar)

        #Eventos
        ###Eventos do Menu
        self.Bind(wx.EVT_MENU, self.OnScore, menuScore)
        self.Bind(wx.EVT_MENU, self.OnRules, menuRules)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        
        ###Eventos dos Botões
        self.botao1.Bind(wx.EVT_BUTTON, self.OnButton)
        self.botao2.Bind(wx.EVT_BUTTON, self.OnButton)
        self.botao3.Bind(wx.EVT_BUTTON, self.OnButton)
        self.botao4.Bind(wx.EVT_BUTTON, self.OnButton)
        self.botao5.Bind(wx.EVT_BUTTON, self.OnButton)
        self.botao6.Bind(wx.EVT_BUTTON, self.OnButton)
        self.botao7.Bind(wx.EVT_BUTTON, self.OnButton)
        self.botao8.Bind(wx.EVT_BUTTON, self.OnButton)
        self.botao9.Bind(wx.EVT_BUTTON, self.OnButton)
        
        
        

    def OnButton(self, event):
        id=event.GetId() #Pega o ID do evento disparado
        button=self.FindWindowById(id) #Retorna o botao que contém o ID do evento disparado;
        if button.GetLabel() == '': #GatLabel - pega o rotulo do botao
            if self.round%2==0:
                button.SetLabel(self.simbolo[0]) #SetLabel - Insere o simbolo no rotulo do botão.
                self.player.SetLabel(f'\n{self.player2}, sua vez')
            else:
                button.SetLabel(self.simbolo[1])
                self.player.SetLabel(f'\n{self.player1}, sua vez')
            self.round+=1

            self.WinGame()

    def WinGame(self):
        getButton = [None,
                     self.botao1.GetLabel(),
                     self.botao2.GetLabel(),
                     self.botao3.GetLabel(),
                     self.botao4.GetLabel(),
                     self.botao5.GetLabel(),
                     self.botao6.GetLabel(),
                     self.botao7.GetLabel(),
                     self.botao8.GetLabel(),
                     self.botao9.GetLabel()
                    ]

        getXButton1 = getButton[1] == 'X'
        getXButton2 = getButton[2] == 'X'
        getXButton3 = getButton[3] == 'X'
        getXButton4 = getButton[4] == 'X'
        getXButton5 = getButton[5] == 'X'
        getXButton6 = getButton[6] == 'X'
        getXButton7 = getButton[7] == 'X'
        getXButton8 = getButton[8] == 'X'
        getXButton9 = getButton[9] == 'X'

        getOButton1 = getButton[1] == 'O'
        getOButton2 = getButton[2] == 'O'
        getOButton3 = getButton[3] == 'O'
        getOButton4 = getButton[4] == 'O'
        getOButton5 = getButton[5] == 'O'
        getOButton6 = getButton[6] == 'O'
        getOButton7 = getButton[7] == 'O'
        getOButton8 = getButton[8] == 'O'
        getOButton9 = getButton[9] == 'O'


        winDlg = None
        

        #Se botao 1, 2 e 3 ou 4, 5 e 6 ou 7, 8 e 9 ou 1, 4 e 7 ou 2, 5 e 8 ou 3, 6 e 9 ou 1, 5 e 9 ou 3, 5 e 7 for X 
        if((getXButton1 and getXButton2 and getXButton3) or (getXButton4 and getXButton5 and getXButton6) or (getXButton7 and getXButton8 and getXButton9) or (getXButton1 and getXButton4 and getXButton7) or (getXButton2 and getXButton5 and getXButton8) or (getXButton3 and getXButton6 and getXButton9) or (getXButton1 and getXButton5 and getXButton9) or (getXButton3 and getXButton5 and getXButton7)):
            print("X ganhou")
            self.player1_score +=1
            winDlg = wx.MessageDialog(self, f'{self.player1} Venceu!', 'Vitória!!')
            
            
        #Se botao 1, 2 e 3 ou 4, 5 e 6 ou 7, 8 e 9 ou 1, 4 e 7 ou 2, 5 e 8 ou 3, 6 e 9 ou 1, 5 e 9 ou 3, 5 e 7 for O 
        elif((getOButton1 and getOButton2 and getOButton3) or (getOButton4 and getOButton5 and getOButton6) or (getOButton7 and getOButton8 and getOButton9) or (getOButton1 and getOButton4 and getOButton7) or (getOButton2 and getOButton5 and getOButton8) or (getOButton3 and getOButton6 and getOButton9) or (getOButton1 and getOButton5 and getOButton9) or (getOButton3 and getOButton5 and getOButton7)):
            print("O ganhou")
            self.player2_score +=1
            winDlg = wx.MessageDialog(self, f'{self.player2} Venceu!', 'Vitória!!')
        
        elif(self.round >= 9):
            print("Velha ganhou")
            self.velha_score +=1
            winDlg = wx.MessageDialog(self, f'A velha venceu essa!', 'Deu velha')


        if winDlg is not None and winDlg.ShowModal() == wx.ID_OK: 
            self.reset_game()
            self.OnScore(None)
        if winDlg is not None:    
            winDlg.Destroy()

    def reset_game(self):
        buttons = [self.botao1, self.botao2, self.botao3,self.botao4, self.botao5, self.botao6, self.botao7, self.botao8, self.botao9]

        #limpa a label dos botoes
        for button in buttons:
            button.SetLabel('')

        #Reinicia as rodadas
        self.round = 0
        self.player.SetLabel(f"{self.player1}, sua vez")
        
        

    def OnScore(self, event):
        dlgScore = wx.MessageDialog(self, f'Pontuação do Jogo Atual\n\n{self.player1} = {self.player1_score}\n{self.player2} = {self.player2_score}\nVelha = {self.velha_score}', 'Pontuação')
        dlgScore.ShowModal()
        dlgScore.Destroy()
        
    def OnRules(self, event):
        dlgAbout = wx.MessageDialog(self, "O objetivo é marcar 3 simbolos iguais em forma vertical, horizontal ou diagonal\nSe nenhum dos dois jogadores conseguirem, a vitória será da velha\nCada jogador terá uma chance, sendo que o Jogador 1 ficará com o X e o jogador 2 ficará com a bola (O).", "Regras do Três em Linha")
        dlgAbout.ShowModal()
        dlgAbout.Destroy()

        
    def OnAbout(self, event):
        dlgAbout = wx.MessageDialog(self, "Jogo da velha Três em Linha desenvolvido por Gabriel Souza, para trabalho do curso de ADS 3° Período", "Sobre o jogo")
        dlgAbout.ShowModal()
        dlgAbout.Destroy()
        
    def OnExit(self, event):
        self.Close(True)

        
class MainApp(wx.App):
    def OnInit(self):
        frame = TicTacFrame(title='Três em Linha')
        frame.Show()
        return True

app = MainApp()
app.MainLoop()
    


    
