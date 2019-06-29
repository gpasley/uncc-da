Attribute VB_Name = "Module1"
Sub stock_tracker_2014()

  Dim stock_name As String
  Dim stock_total As Double
  Dim summary_row As Integer

  stock_total = 0
  summary_row = 2
  
  For i = 2 To 705714
    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
      stock_name = Cells(i, 1).Value
      stock_total = stock_total + Cells(i, 7).Value
      Range("I" & summary_row).Value = stock_name
      Range("J" & summary_row).Value = stock_total
      summary_row = summary_row + 1
      stock_total = 0
    Else
      stock_total = stock_total + Cells(i, 7).Value
    End If
  Next i

End Sub

Sub stock_tracker_2015()

  Dim stock_name As String
  Dim stock_total As Double
  Dim summary_row As Integer

  stock_total = 0
  summary_row = 2
  
  For i = 2 To 760192
    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
      stock_name = Cells(i, 1).Value
      stock_total = stock_total + Cells(i, 7).Value
      Range("I" & summary_row).Value = stock_name
      Range("J" & summary_row).Value = stock_total
      summary_row = summary_row + 1
      stock_total = 0
    Else
      stock_total = stock_total + Cells(i, 7).Value
    End If
  Next i
End Sub


Sub stock_tracker_2016()

  Dim stock_name As String
  Dim stock_total As Double
  Dim summary_row As Integer

  stock_total = 0
  summary_row = 2
  
  For i = 2 To 797711
    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
      stock_name = Cells(i, 1).Value
      stock_total = stock_total + Cells(i, 7).Value
      Range("I" & summary_row).Value = stock_name
      Range("J" & summary_row).Value = stock_total
      summary_row = summary_row + 1
      stock_total = 0
    Else
      stock_total = stock_total + Cells(i, 7).Value
    End If
  Next i

End Sub




