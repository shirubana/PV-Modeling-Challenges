PVObject_=pvModule
  Version=7.0.4
  Flags=$00500043

  PVObject_Commercial=pvCommercial
    Comment=www.trinasolar.com (China)
    Flags=$0041
    Manufacturer=Trina Solar
    Model=TSM-600DE20
    DataSource=UL 2020
    YearBeg=2020
    Width=1.303
    Height=2.172
    Depth=0.035
    Weight=30.900
    NPieces=100
    PriceDate=24/04/19 10:39
    Currency=EUR
    Remarks, Count=2
      Str_1
      Str_2
    End of Remarks
  End of PVObject pvCommercial

  Technol=mtSiMono
  NCelS=60
  NCelP=2
  NDiode=3
  SubModuleLayout=slTwinHalfCells
  GRef=1000
  TRef=25.0
  PNom=600.0
  PNomTolLow=0.00
  PNomTolUp=3.00
  Isc=18.520
  Voc=41.50
  Imp=17.440
  Vmp=34.40
  muISC=7.41
  muVocSpec=-115.8
  muPmpReq=-0.363
  RShunt=160
  Rp_0=4000
  Rp_Exp=3.20
  RSerie=0.124
  Gamma=1.051
  muGamma=-0.0004
  VMaxIEC=1500
  VMaxUL=1500
  Absorb=0.90
  ARev=3.200
  BRev=12.168
  RDiode=0.010
  VRevDiode=-0.70
  AirMassRef=1.500
  CellArea=220.5
  SandiaAMCorr=50.000
  RelEffic800=0.58
  RelEffic600=0.72
  RelEffic400=0.25
  RelEffic200=-1.72

  PVObject_IAM=pvIAM
    Flags=$00
    IAMMode=UserProfile
    IAMProfile=TCubicProfile
      NPtsMax=9
      NPtsEff=9
      LastCompile=$B18D
      Mode=3
      Point_1=0.0,1.00000
      Point_2=30.0,1.00000
      Point_3=50.0,0.99900
      Point_4=60.0,0.99500
      Point_5=70.0,0.97500
      Point_6=75.0,0.93900
      Point_7=80.0,0.84600
      Point_8=85.0,0.60900
      Point_9=90.0,0.00000
    End of TCubicProfile
  End of PVObject pvIAM

  OperPoints, list of=4 tOperPoint
    Point_1=False,800,25.0,0.58,0.00,0.000,0.000,0.00
    Point_2=False,600,25.0,0.72,0.00,0.000,0.000,0.00
    Point_3=False,400,25.0,0.25,0.00,0.000,0.000,0.00
    Point_4=False,200,25.0,-1.72,0.00,0.000,0.000,0.00
  End of List OperPoints
End of PVObject pvModule
