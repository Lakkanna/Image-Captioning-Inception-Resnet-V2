import wx
import test as t
class MyFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title="Image Description- Evaluation", size=(400,-1))
		self.panel = wx.Panel(self)
		self.result = ''
		self.caption = ''
		self.path = ''
		#self.image = wx.StaticBitmap(self.panel, -1, wx.Bitmap('test/image.jpg', wx.BITMAP_TYPE_ANY), pos = wx.Point(0, 0), size = (400,200))
		
		self.openFileDialog = wx.FileDialog(self.panel,"Choose a file", "test/", "","",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		self.filebutton = wx.Button(self.panel,label = 'Open file', pos = (70,35),size=(80,40))
		self.Bind(wx.EVT_BUTTON,self.openfile, self.filebutton)
		self.button = wx.Button(self.panel,label = 'Get Caption', pos = (230,35),size=(100,40))
		self.Bind(wx.EVT_BUTTON,self.changed, self.button)
		 
       		self.p =  wx.StaticText(self.panel,label = "", pos = (5,85))
		self.p.SetFont(wx.Font(10,wx.SWISS, wx.NORMAL, wx.BOLD))
        	self.p.SetSize(self.p.GetBestSize())
		self.c =  wx.StaticText(self.panel,label = "", pos = (5,400))
		self.c.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        	self.c.SetSize(self.c.GetBestSize())
		self.status = wx.StaticText(self.panel,label = self.result, pos = (50,85),size=(70,20))
		self.output = wx.StaticText(self.panel,label = self.caption, pos = (85,400))
		self.Centre()
	def openfile(self,event):
		if self.openFileDialog == wx.ID_CANCEL:
			return
		self.openFileDialog.ShowModal()
		self.path = self.openFileDialog.GetPath()
		self.c.SetLabel(" ")
		self.output.SetLabel(" ")
		#self.openFileDialog.Destroy()
		self.p.SetLabel('path: ')
		self.status.SetLabel(self.path)
		self.img = wx.Image(self.path,wx.BITMAP_TYPE_ANY).Rescale(400,250).ConvertToBitmap()
		wx.StaticBitmap(self.panel, -1, self.img, (0,120), (self.img.GetWidth(), self.img.GetHeight()))
		
	def changed(self, event):
		#self.result = t.text("test/image.jpg")
		if(self.path):
			self.caption  = t.text(self.path)
			self.c.SetLabel('caption: ')
			self.output.SetLabel(self.caption)
			self.output.SetFont(wx.Font(10,wx.SWISS, wx.NORMAL,wx.NORMAL))
        		self.output.SetSize(self.output.GetBestSize())
		else:
			self.p.SetLabel('path: ')
			self.status.SetLabel('Select image to evaluate...!')

app = wx.App(False)
frame = MyFrame(None, "Hello")
frame.Show()
app.MainLoop()
		
