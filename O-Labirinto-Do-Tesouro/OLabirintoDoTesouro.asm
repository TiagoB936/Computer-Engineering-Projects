INCLUDE ..\Irvine32.inc

;Tiago Bachiega de Almeida 628247
;Guilherme Nishi Kanashiro 628298
.data
mapa BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE 0Ah,0Dh,"H","P",20h,20h,"T","H",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h
      BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h
      BYTE "o","H",0Ah,0Dh,"H",20h,20h,20h,20h,"H",20h,20h,"H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H",20h,20h,"H"
      BYTE "H","H","H","H",0Ah,0Dh,"H",20h,20h,20h,20h,"H",20h,20h,"H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","T",20h,"H","H","H","H","H","H","H","H","H","H","T"
      BYTE 20h,"H","H","H","H","H",0Ah,0Dh,"H",20h,20h,20h,20h,20h,20h,20h,"H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H",20h,20h,20h,20h,"H","H","H","H","H","H","H"
      BYTE "H",20h,20h,"H","H","H","H","H",0Ah,0Dh,"H",20h,20h,"H","H","H",20h,20h,"H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H",20h,20h,20h,"o","H","H","H","H","H"
      BYTE "H","H","H",20h,20h,"H","H","H","H","H",0Ah,0Dh,"H","o",20h,20h,"T","H",20h,20h,20h,20h,20h,"H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H",20h,20h,"H","H","H","H","H",0Ah,0Dh,"H","H","H","H","H","H",20h,20h,20h,20h,20h
      BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H",20h,20h,"H","H","H","H","H",0Ah,0Dh,"H","H","H","H","H","H","H","H","H"
      BYTE "H",20h,20h,"H","H","H","H","H","H","H","H","H",20h,20h,"H",20h,20h,"H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H",20h,20h,"H","H","H","H","H",0Ah,0Dh,"H","o",20h,20h,"H","H","H"
      BYTE "H","H","H",20h,20h,"H","H","H","H","H","H","H","H","H",20h,20h,"T",20h,20h,20h,20h,20h,20h,20h,20h
      BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"o","H","H","H","H",0Ah,0Dh,"H",20h,20h,"T","H"
      BYTE "H","H","H","H","H",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"H",20h,20h,"H",20h,20h,"H","H","H","H"
      BYTE "H","H",20h,"H","H","H","H","H","H","H","H","H","H",20h,"H","H","H","H","H","H",0Ah,0Dh,"H",20h,"H"
      BYTE 20h,"H","H","H","H","H","H",20h,20h,"H","H","H","H","H","H","H",20h,"H",20h,20h,20h,20h,20h,"H","H"
      BYTE "H","H","H","H",20h,20h,"H","H","H","H","H","H","H","H","H",20h,"H","H","H","H","H","H",0Ah,0Dh,"H"
      BYTE 20h,20h,20h,"H","H","H","H","H","H",20h,20h,"H","H","H","H","H","H","H",20h,"H","H","H",20h,"H","H"
      BYTE "H","H","H","H","H","H","H",20h,"H","H","H","H","H","H","H","H","H",20h,"H","H","H","H","H","H",0Ah
      BYTE 0Dh,"H","H","H","H","H","H","H","H","H","H",20h,20h,"H","H","H","H","H","H","H",20h,"H","H","H",20h
      BYTE "H","H","H","H","H","H","H","H","H",20h,"H","H","H","H","H",20h,20h,20h,20h,20h,20h,20h,"T","H","H"
      BYTE "H",0Ah,0Dh,"H","o",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"H","H","H","H","H","H","H",20h,"H","H"
      BYTE "H",20h,"H","H","H","H","H","H","H","H","H",20h,"H","H","H","H","H","H","H","H","H","H","H",20h,"H"
      BYTE "H","H","H",0Ah,0Dh,"H","H",20h,20h,"H","H","H","H","H","H","H","H","H","H","H","H","H","H","H",20h
      BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"H","H","H","H","H","H","H","H"
      BYTE 20h,"H","H","H","H",0Ah,0Dh,"H","H",20h,20h,"H","H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H",20h,"H","H","H",20h,"H","H","H","H","H","H","H","H","H","H","H",20h,20h,20h,20h,20h,20h,"H","H"
      BYTE "H","H",20h,"H","H","H","H",0Ah,0Dh,"H","H",20h,20h,"H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H",20h,"H","H","H",20h,"H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H",20h,"H","H","H","H",0Ah,0Dh,"H","H",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h
      BYTE 20h,20h,20h,20h,20h,20h,20h,"H","H",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"o",20h,20h,"T",20h,20h
      BYTE 20h,20h,"H","H","H","H","o",20h,20h,"T","H",0Ah,0Dh,"H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H",0Ah,0Dh,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h


mapa1 BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H"
     BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H"
     BYTE 0Ah,0Dh,"H","P",20h,20h,20h,"H",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h
     BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"o",20h,20h,20h
     BYTE "T","H",0Ah,0Dh,"H","H","H",20h,20h,20h,20h,"H","H","H","H","H","H","H","H","H","H","H","H","H",20h
     BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H",20h,"H","H","H","H","H","H","H","H","H","H","H"
     BYTE 20h,20h,"H","H",0Ah,0Dh,"H","H","H",20h,"H","H","H","H","H","H","H","H","H",20h,20h,20h,20h,20h,"H"
     BYTE "H",20h,"T","H","H","H","H","H","H","H","H","H","H","H","H",20h,"H","H","H","H","H","H","H","H","H"
     BYTE "H","H",20h,20h,"H","H",0Ah,0Dh,"H",20h,20h,20h,20h,20h,20h,20h,"H","H","H","H","H",20h,"H","H","H"
     BYTE "H","H","H",20h,20h,20h,"o","H","H","H",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"H","H","H"
     BYTE "H","H","H","H",20h,20h,"H","H",0Ah,0Dh,"H",20h,20h,"H","H","H","H",20h,"H","H","H","H","H",20h,20h
     BYTE 20h,20h,20h,"H","H",20h,"H","H","H","H","H","H",20h,20h,"H","H","H","H","H","H","H","H","H",20h,"H"
     BYTE "H","H","H","H","H","H",20h,20h,"H","H",0Ah,0Dh,"H",20h,20h,"H","o",20h,"H",20h,"H","H","H","H","H"
     BYTE "H","H","H",20h,20h,20h,20h,20h,"H","H","H","H","H","H",20h,20h,"H",20h,20h,20h,20h,20h,20h,"H","H"
     BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"H","H",0Ah,0Dh,"H",20h,20h,"H",20h,20h,20h,20h,20h,20h,20h
     BYTE 20h,"H","H","H","H","H","H","H","H",20h,"H","H","H","H","H","H",20h,20h,"H",20h,20h,20h,20h,"H",20h
     BYTE "H","H","H","H","H","H","H","H",20h,20h,"H","H","H","H",0Ah,0Dh,"H",20h,20h,"H","H","H","H","H","H"
     BYTE "H",20h,20h,"H","o",20h,20h,20h,"H","H","H",20h,"H","H","H","H","H","H",20h,20h,"H","H","H","H","H"
     BYTE "H",20h,"H","H","H","H","H","H","H","H",20h,20h,"H","H","H","H",0Ah,0Dh,"H",20h,20h,"H","H",20h,"T"
     BYTE 20h,"o","H",20h,20h,"H","H","H","H",20h,"H","H","H",20h,"H","H","H","H","H","H",20h,20h,20h,20h,20h
     BYTE 20h,20h,20h,20h,"H","H","H","H","H","H","H","H",20h,20h,"H","H","H","H",0Ah,0Dh,"H",20h,"T","H","H"
     BYTE 20h,"H","H","H","H",20h,20h,"H","H","H","H",20h,20h,20h,20h,20h,20h,20h,20h,20h,"T","H","H","H","H"
     BYTE "H","H","H","H","H",20h,"H","H","H","H","H","H","H","H",20h,20h,"H","o",20h,"H",0Ah,0Dh,"H","H","H"
     BYTE "H","H",20h,20h,20h,20h,20h,20h,20h,"H","H","H","H","H","H","H","H","H","H",20h,20h,"H","H","H","H"
     BYTE "H","H",20h,20h,20h,20h,20h,20h,"H","H","H","H","H","H","H","H",20h,20h,"H","H",20h,"H",0Ah,0Dh,"H"
     BYTE "H","H","H","H","H","H","H","H","H","H",20h,"H","H","H","H","H","H","H","H","H","H",20h,20h,"H","H"
     BYTE "H","H","H","H",20h,"H","H","H","H",20h,"H","H","H","H","H","H","H","H",20h,20h,"H","T",20h,"H",0Ah
     BYTE 0Dh,"H","H","H","H","H","H","H","H","H","H","H",20h,"H","H","H","H","H","H","H","H","H","H",20h,20h
     BYTE 20h,20h,20h,20h,20h,"H",20h,"H","o",20h,"H",20h,"H","H","H","H","H","H","H","H",20h,20h,"H",20h,20h
     BYTE "H",0Ah,0Dh,"H",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"H","H","H","H","H","H","H","H","H","H"
     BYTE "H","H","H","H","H",20h,20h,"H",20h,20h,20h,"T","H",20h,"H","H","H","H","H","H","H","H",20h,20h,20h
     BYTE 20h,20h,"H",0Ah,0Dh,"H",20h,20h,"H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H"
     BYTE "H","H","H","H",20h,20h,"H",20h,20h,"H","H","H","H","H","H",20h,"H","H","H","H","H","H","H","H","H"
     BYTE "H","H","H","H","H",0Ah,0Dh,"H",20h,20h,"H","H","H","H","H",20h,20h,20h,"H","H","H","H",20h,20h,20h
     BYTE 20h,20h,"T","H","H","H",20h,20h,"H",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"H","H","H"
     BYTE "H","H","H","H","H","H","H",0Ah,0Dh,"H",20h,20h,"H","H","H","H","H",20h,"H",20h,"H","H","H",20h,20h
     BYTE 20h,"H",20h,20h,20h,"H","H","H",20h,20h,"H",20h,20h,"H","H","H","H","H","H","H","H","H","H",20h,"H"
     BYTE "H","H","H","H","H","H","H","H","H",0Ah,0Dh,"H",20h,20h,20h,20h,20h,20h,20h,20h,"H",20h,20h,20h,20h
     BYTE 20h,20h,20h,"H",20h,20h,"o","H","H","H",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h
     BYTE 20h,20h,20h,20h,20h,20h,"o",20h,20h,"T","H",0Ah,0Dh,"H","H","H","H","H","H","H","H","H","H","H","H"
     BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H"
     BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H",0Ah,0Dh,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h

mapa2 BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE 0Ah,0Dh,"H","P",20h,20h,"T","H",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h
      BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h
      BYTE "o","H",0Ah,0Dh,"H",20h,20h,20h,20h,"H",20h,20h,"H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H",20h,20h,"H"
      BYTE "H","H","H","H",0Ah,0Dh,"H",20h,20h,20h,20h,"H",20h,20h,"H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","T",20h,"H","H","H","H","H","H","H","H","H","H","T"
      BYTE 20h,"H","H","H","H","H",0Ah,0Dh,"H",20h,20h,20h,20h,20h,20h,20h,"H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H",20h,20h,20h,20h,"H","H","H","H","H","H","H"
      BYTE "H",20h,20h,"H","H","H","H","H",0Ah,0Dh,"H",20h,20h,"H","H","H",20h,20h,"H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H",20h,20h,20h,"o","H","H","H","H","H"
      BYTE "H","H","H",20h,20h,"H","H","H","H","H",0Ah,0Dh,"H","o",20h,20h,"T","H",20h,20h,20h,20h,20h,"H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H",20h,20h,"H","H","H","H","H",0Ah,0Dh,"H","H","H","H","H","H",20h,20h,20h,20h,20h
      BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H",20h,20h,"H","H","H","H","H",0Ah,0Dh,"H","H","H","H","H","H","H","H","H"
      BYTE "H",20h,20h,"H","H","H","H","H","H","H","H","H",20h,20h,"H",20h,20h,"H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H",20h,20h,"H","H","H","H","H",0Ah,0Dh,"H","o",20h,20h,"H","H","H"
      BYTE "H","H","H",20h,20h,"H","H","H","H","H","H","H","H","H",20h,20h,"T",20h,20h,20h,20h,20h,20h,20h,20h
      BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"o","H","H","H","H",0Ah,0Dh,"H",20h,20h,"T","H"
      BYTE "H","H","H","H","H",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"H",20h,20h,"H",20h,20h,"H","H","H","H"
      BYTE "H","H",20h,"H","H","H","H","H","H","H","H","H","H",20h,"H","H","H","H","H","H",0Ah,0Dh,"H",20h,"H"
      BYTE 20h,"H","H","H","H","H","H",20h,20h,"H","H","H","H","H","H","H",20h,"H",20h,20h,20h,20h,20h,"H","H"
      BYTE "H","H","H","H",20h,20h,"H","H","H","H","H","H","H","H","H",20h,"H","H","H","H","H","H",0Ah,0Dh,"H"
      BYTE 20h,20h,20h,"H","H","H","H","H","H",20h,20h,"H","H","H","H","H","H","H",20h,"H","H","H",20h,"H","H"
      BYTE "H","H","H","H","H","H","H",20h,"H","H","H","H","H","H","H","H","H",20h,"H","H","H","H","H","H",0Ah
      BYTE 0Dh,"H","H","H","H","H","H","H","H","H","H",20h,20h,"H","H","H","H","H","H","H",20h,"H","H","H",20h
      BYTE "H","H","H","H","H","H","H","H","H",20h,"H","H","H","H","H",20h,20h,20h,20h,20h,20h,20h,"T","H","H"
      BYTE "H",0Ah,0Dh,"H","o",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"H","H","H","H","H","H","H",20h,"H","H"
      BYTE "H",20h,"H","H","H","H","H","H","H","H","H",20h,"H","H","H","H","H","H","H","H","H","H","H",20h,"H"
      BYTE "H","H","H",0Ah,0Dh,"H","H",20h,20h,"H","H","H","H","H","H","H","H","H","H","H","H","H","H","H",20h
      BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"H","H","H","H","H","H","H","H"
      BYTE 20h,"H","H","H","H",0Ah,0Dh,"H","H",20h,20h,"H","H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H",20h,"H","H","H",20h,"H","H","H","H","H","H","H","H","H","H","H",20h,20h,20h,20h,20h,20h,"H","H"
      BYTE "H","H",20h,"H","H","H","H",0Ah,0Dh,"H","H",20h,20h,"H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H",20h,"H","H","H",20h,"H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H",20h,"H","H","H","H",0Ah,0Dh,"H","H",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h
      BYTE 20h,20h,20h,20h,20h,20h,20h,"H","H",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,"o",20h,20h,"T",20h,20h
      BYTE 20h,20h,"H","H","H","H","o",20h,20h,"T","H",0Ah,0Dh,"H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H"
      BYTE "H","H","H","H","H","H","H","H","H","H","H","H","H",0Ah,0Dh,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h

    
menu BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,"O",20h,"L","A","B","I","R","I","N","T","O",20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,"D","O",20h,"T","E","S","O","U","R","O",20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,3Eh,"J","O","G","A","R",20h,20h,"W",20h,"C","I","M","A",20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,"S","A","I","R",20h,20h,20h,"S",20h,"B","A","I","X","O",0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,"G","U","I","A",20h,20h,20h,"O",20h,"O","K",20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    
telaDific BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,3Eh,"F","A","C","I","L",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,"M","E","D","I","O",20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,"D","I","F","I","C","I","L",20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
    BYTE 20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,20h,0Ah,0Dh
         
    
;Dimensoes das matrizes que representam os mapas
qntLinhasMenu = 12
qntColunasMenu = 21
qntLinhasMapa = 20		;Quantidade de linhas da matriz
qntColunasMapa = 52 	;Quantidade de colunas da matriz
	
instrucoes1 BYTE "WASD - Movimentacao", 0Ah, 0Dh, 0
instrucoes2 BYTE "Pegue os tesouros (o) e leve para a saida.", 0Ah, 0Dh, 0
instrucoes3 BYTE "Cuidado! Seus movimentos sao limitados" , 0Ah, 0Dh, 0
instrucoes4 BYTE "Use os tuneis (SpaceBar) para gastar menos movimentos:" ,0Ah, 0Dh,0
instrucoes5 BYTE "Cada tunel (T) te leva para o outro da mesma cor.", 0Ah, 0Dh, 0Ah, 0Dh, 0
instrucoes6 BYTE "A - Voltar", 0Ah, 0Dh,0

msgProxFase BYTE "Fase 2",0Ah,0Dh,0Ah,0Dh,0Ah,0Dh,0Ah,0Dh,"O - ontinuar",0Ah,0Dh,0
msgGameOver BYTE "Game Over",0Ah,0Dh,0
msgZerouJogo BYTE "Parabens! Voce concluiu o jogo",0Ah,0Dh,0Ah,0Dh,"Tiago Bachiega de Almeida",
					0Ah,0Dh, "Guilherme Nishi Kanashiro",0Ah,0Dh,0

tesourosStr BYTE "Tesouros: ",0 ;String para o contador de tesourosRestantes
movimentosStr1 BYTE "Movimentos Disponiveis: ",0 
movimentosStr2 BYTE "Movimentos Feitos: ",0 
   
tuneis BYTE  6,9,47,12, 25,10,48,18, 20,16,33,14, 2,10,21,3 ,48,1	;array com posicao dos tuneis 
qntTuneis DWORD ? 	;quantidade de tuneis/2
TunelFinal DWORD ?
tesourosRestantes DWORD ?;Conta os tesouros restantes

;Dados referente a fase 1/mapa 1
tuneis1 BYTE 6,9,47,12,25,10,48,18,20,16,33,14,2,10,21,3,48,1
qntTuneis1 DWORD 4
TunelFinal1 DWORD 100
tesourosRestantes1 DWORD 9
movMapa1Facil BYTE 250
movMapa1Medio BYTE 225
movMapa1Dificil BYTE 210

;Dados referente a fase 2/mapa 2
tuneis2 BYTE 4,6,3,10,4,1,43,3,31,3,23,9,46,13,36,18,48,18
qntTuneis2 DWORD 4
TunelFinal2 DWORD 984
tesourosRestantes2 DWORD 8
movMapa2Facil BYTE 200
movMapa2Medio BYTE 185
movMapa2Dificil BYTE 170

posiSeta DWORD 172
xp DWORD 1 				;posicao x do jogador
yp DWORD 1 				;posicao y do jogador

comando BYTE ?			;Comando inserido pelo usuario
movFeitos BYTE ?		;Conta os movimentos restantes
movDificuldade BYTE ?

;Sinais de controle durante a execucao do jogo
sinalMapa BYTE 0 			;d,w,a,s-> nao colidiu (direcao), 1 -> parede ou nao se move, 2 -> entra no tunel
sinalTesouro BYTE 0			;Diz se encostou em um tesouro
sinalTunel BYTE 0			;T-> o personagem está em cima do tunel, 0-> o personagem não está em cima do tunel, 1 -> o personagem usou o tunel
sinalMenu BYTE 0
sinalDificuldade BYTE ? 	;1-facil, 2-normal. 3-dificil
sinalFase BYTE 1 			;1->fase 1, 2-> fase 2, 0 -> acabou

cursorPosi COORD <0,0>
cHandle DWORD ?
curInf CONSOLE_CURSOR_INFO <100d, 00000000h>

;Variáveis de definicao das cores dos elementos do mapa
corPadrao = lightGray + (black * 16)
corMoeda = yellow + (black*16)
corJogador = lightred + (black*16)
corParede = brown + (brown*16)
corT1 = lightgreen + (black*16)
corT2 = lightblue + (black*16)
corT3 = lightmagenta + (black*16)
corT4 = lightcyan + (black*16)
corFinal = white + (black*16)
corTunel BYTE corT1,corT1,corT2,corT2,corT3,corT3,corT4,corT4,	;Array com a cor dos pares de túneis

.code
main PROC  
    
    Invoke GetStdHandle, STD_OUTPUT_HANDLE
    mov cHandle, eax
    mov eax, 0
    
	;Esconde o cursor
	Invoke setConsoleCursorInfo, cHandle, OFFSET curInf
	
    call telaInicial
        
    cmp sinalMenu, 1
    jne sair ;fecha o jogo
    
    mov posiSeta, 45
    
    call telaDificuldade

setaDificuldade:    
    ;Ajuste de dificuldade
    cmp sinalDificuldade,1
    je setarFacil
    cmp sinalDificuldade,2 
    je setarMedio
    cmp sinalFase,2 ;Seta os movimentos da primeira fase
    je setaFase2Dificil 
    mov al, movMapa1Dificil
    mov movDificuldade, al
    mov al,0
    jmp comecaJogo
    setaFase2Dificil: ;Seta os movimentos se for segunda fase
    mov al, movMapa2Dificil
    mov movDificuldade,al
    mov al,0
    jmp comecaJogo

    setarFacil:
        cmp sinalFase,2
        je setaFase2Facil
        mov al, movMapa1Facil
        mov movDificuldade, al
        mov al,0
        jmp comecaJogo
        setaFase2Facil:
        mov al, movMapa2Facil
        mov movDificuldade,al
        mov al,0
        jmp comecaJogo
    setarMedio:
        cmp sinalFase,2
        je setaFase2Medio
        mov al, movMapa1Medio
        mov movDificuldade, al
        mov al,0
        jmp comecaJogo
        setaFase2Medio:
        mov al, movMapa2Medio
        mov movDificuldade,al
        mov al,0

comecaJogo:

    call inicializacoes
	
LoopPrincipal:
	
    ;Imprime o mapa
    Invoke setconsolecursorposition, cHandle, cursorPosi
    mov eax, 0
    mov ecx, qntLinhasMapa*qntColunasMapa
    mov esi, 0
    
    ;Loop da impressao do mapa
    LoopMapa:
		
        call setCor	
        
    print:
        mov al, mapa[esi]
        call WriteChar
        add esi, TYPE mapa
        
    loop LoopMapa
    
NImprime:   

    ;Espera a insercao de um caractere
    call ReadChar
    mov comando, al
    
    call processaMovimento
    
    ;Se nao for possivel se mover, retorna para o inicio
    cmp sinalMapa, 1
    je NImprime
    
    call atualizaMapa
    
    ;Segunda fase
    cmp sinalFase,2
    je setaDificuldade
    
    ;GAME OVER
    mov al, movDificuldade
    cmp movFeitos,al
    jne loopPrincipal
    call gameOver

sair:
	exit
main ENDP


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Função: muda a cor do caractere as ser impresso de acordo
; 		 com o elemento do mapa a ser impresso
;Recebe: esi(posicao do mapa a ser impresso), mapa[esi](elemento)
;Retorna: a alteracao na cor do caracter de acordo com o elemento 
;Requer: -
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

setCor PROC
	cmp mapa[esi], "o"
	je moeda
	cmp mapa[esi],"P"
	je jogador
	cmp mapa[esi],"H"
	je parede
	cmp mapa[esi],"T"
	je tunel
	jmp espaco			;nenhuma das outras opções
	
	;set cor moedas 
	moeda:
        mov al,corMoeda
        movzx  eax,al
        call SetTextColor
        jmp sair
        
	;set cor jogador	
    jogador:
        mov al, corJogador
        movzx eax, al
        call SetTextColor
        jmp sair
		
    ;set cor parede 
    parede:
        mov al, corParede
        movzx eax, al
        call SetTextColor
        jmp sair
		
	;set cor do tunel	
	tunel:
		cmp esi,tunelFinal
		je espaco
		push ecx
		call procuraTunel		;retorna a posição do tunel no vetor de tuneis
		shr edi,1				;divide edi por 2 -- no vetor de tuneis as coordenadas sempre ocupam duas posições 
		mov al, corTunel[edi]
		movzx eax, al
		call SetTextColor
		pop ecx
		jmp sair
		
	espaco:
		;set cor padrao
        mov al,corPadrao
        movzx  eax,al
        call SetTextColor
		
	sair:	
		ret
setCor ENDP

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Funcao: testar se o jogador chegou ao final da fase
;		 ou se ele chegou ao fim do jogo
;Recebe: sinalFase
;Retorna: proxima acao dependendo em que fase o jogador esta
;Requer: jogador tenha atingido um túnel final
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
proximaFase proc

    ;Terminou a fase
    cmp sinalFase,1
    je proxFase
    
    ;Zerou o jogo
    call Clrscr
        
    mov edx, OFFSET msgZerouJogo
    call WriteString
    
    call ReadChar
    
	exit
    
    ;Fase 2
    proxFase:
        call Clrscr
        
        mov edx, OFFSET msgProxFase
        call WriteString
        
        
        leDnv:
            call ReadChar
            mov comando, al
            
            cmp comando, "o"
            jne leDnv
            
        mov sinalFase,2
        
        call Clrscr
    ret
proximaFase endp

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Funcao: mostrar mensagem de fim de jogo
;Recebe: mensagem de fim de jogo
;Retorna: - 
;Requer: uma das condicoes de fim de jogo seja atingida
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
gameOver proc

    call Clrscr
    
    mov edx, OFFSET msgGameOver
    call WriteString
    
    call ReadChar
    
    exit
    
    ret
gameOver endp


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Funcao: inicializa as variáveis e sinais importantes para o
;comeco do jogo
;Recebe: todas as variaveis a serem inicializadas
;Retorna: sinal de inicio de fase
;Requer: que alguma fase seja inicializada
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
inicializacoes proc

    ;Dificuldade (movimentos)
    mov al, movDificuldade
    mov movFeitos, 0
    
    mov al,0

    ;Inicializaca fase
    mov ecx, qntColunasMapa*qntLinhasMapa
    mov esi, 0
    
    cmp sinalFase,1
    je fase1
    jmp fase2
    
    ;fase 1
fase1:

    LoopMapaFase1:      
        mov al, mapa1[esi]
        mov mapa[esi], al
        add esi, TYPE mapa
    loop LoopMapaFase1
    
    mov ecx, LENGTHOF tuneis1
    mov esi, 0
    
    LoopTunel1:
        
        mov al, tuneis1[esi]
        mov tuneis[esi], al
        add esi, TYPE tuneis
    loop LoopTunel1
    
    mov eax, qntTuneis1
    mov qntTuneis, eax
    
    mov eax, TunelFinal1
    mov TunelFinal, eax
    
    mov eax, tesourosRestantes1
    mov tesourosRestantes, eax
    
    jmp sair
    
fase2:    
    ;fase2
    LoopMapaFase2:
    
        mov al, mapa2[esi]
        mov mapa[esi], al
        add esi, TYPE mapa
    loop LoopMapaFase2
    
    mov ecx, LENGTHOF tuneis1
    mov esi, 0
    
    LoopTunel2:
        mov al, tuneis2[esi]
        mov tuneis[esi], al
        add esi, TYPE tuneis
    loop LoopTunel2
    
    mov eax, qntTuneis2
    mov qntTuneis, eax
    
    mov eax, TunelFinal2
    mov TunelFinal, eax
    
    mov eax, tesourosRestantes2
    mov tesourosRestantes, eax
    
    mov sinalFase,0
    
sair:    
    mov al, 0
    mov xp, 1
    mov yp, 1
    
    ret
inicializacoes endp

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;FUNCAO: exibir a tela de dificuldade e selecinar a dificuldade do jogo
;Recebe: matriz da tela de dificuldade
;Retorna: sinalDificuldade
;Requer: o jogador selecionou jogar na tela inicial
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
telaDificuldade proc
    
    call Clrscr
    
start: 

    Invoke setconsolecursorposition, cHandle, cursorPosi
    
    mov ecx, qntColunasMenu*qntLinhasMenu
    mov al, 0
    mov esi, 0
    
    LoopTelaDif:
    
        mov al, telaDific[esi]
        call WriteChar
        
        add esi, TYPE telaDific
    
    loop LoopTelaDif

    mov esi, posiSeta
    
    call ReadChar
    mov comando, al
    
    cmp comando, "o" ;Selecionou algo
    je selecao
    cmp comando, "s" ;Move cursor para baixo
    je teclaS
    cmp comando, "w" ; Move cursor para cima
    je teclaW
    jmp start
        
selecao:
    cmp telaDific[esi + qntColunasMenu], 3Eh
    je medio 
    cmp telaDific[esi + qntColunasMenu + qntColunasMenu], 3Eh
    je dificil
    mov sinalDificuldade, 1
    jmp sair 
    
    medio:
        mov sinalDificuldade, 2
        jmp sair
    dificil:
        mov sinalDificuldade, 3
        jmp sair
    
teclaS: ; Move o cursor para baixo
    cmp telaDific[esi], 3Eh
    je segundaOpS
    jmp terceiraOpS
    segundaOpS: ;Estava na primeira opcao, move para a segunda
        mov telaDific[esi], 20h
        mov telaDific[esi + qntColunasMenu], 3Eh
        jmp start
    terceiraOpS: ;Estava na segunda opcao, move para a terceira
        mov telaDific[esi + qntColunasMenu], 20h
        mov telaDific[esi + qntColunasMenu + qntColunasMenu], 3Eh
        jmp start
teclaW: ; Move o cursor para cima
    cmp telaDific[esi + qntColunasMenu + qntColunasMenu], 3Eh
    je segundaOpW 
    jmp primeiraOpW
    primeiraOpW: ;Estava na segunda opcao, move par a primeira
        mov telaDific[esi], 3Eh
        mov telaDific[esi + qntColunasMenu], 20h
        jmp start
    segundaOpW: ;Estava na terceira opcao, move para a segunda
        mov telaDific[esi + qntColunasMenu], 3Eh
        mov telaDific[esi + qntColunasMenu + qntColunasMenu], 20h
        jmp start
    
sair:
    call Clrscr
    ret
    
telaDificuldade endp

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;FUNCAO : realiza a impressão e a logica da tela inicial do jogo
;Recebe: al(comando do jogador)
;Retorna: a tela solicitada pelo jogador
;Requer: nada
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
telaInicial proc
    call Clrscr
start:

    Invoke setconsolecursorposition, cHandle, cursorPosi
    mov ecx, qntColunasMenu*qntLinhasMenu
    mov al, 0
    mov esi, 0
    
    ;Imprime o menu
    LoopMenu:
        
        mov al, menu[esi]
        call WriteChar
        
        add esi, TYPE menu
    
    Loop LoopMenu
    
    mov esi, posiSeta
    
    call ReadChar
    mov comando, al
    
    cmp comando, "o" ;Selecionou algo
    je selecao
    cmp comando, "s" ;Move cursor para baixo
    je teclaS
    cmp comando, "w" ; Move cursor para cima
    je teclaW
    jmp start
    
selecao:
    cmp menu[esi + qntColunasMenu], 3Eh
    je sair ; selecionou sair
    cmp menu[esi + qntColunasMenu + qntColunasMenu], 3Eh
    je abreInstrucoes
    mov sinalMenu, 1 ;selecionou jogar
    jmp sair 
    abreInstrucoes:
    
        ;Imprime todas as instrucoes
        call Clrscr
        mov edx,0
        mov edx, OFFSET instrucoes1
        call WriteString
        mov edx, OFFSET instrucoes2
        call WriteString
        mov edx, OFFSET instrucoes3
        call WriteString
        mov edx, OFFSET instrucoes4
        call WriteString
        mov edx, OFFSET instrucoes5
        call WriteString
        mov edx, OFFSET instrucoes6
        call WriteString
        
        ;Se nao inseriu o comando de volta corretamente, pede de novo
        nenhumaInstrucao:
            mov al, 0
            call ReadChar
            mov comando, al
            
            cmp comando, "a"
            jne nenhumaInstrucao
            call Clrscr
            jmp start
teclaS: ; Move o cursor para baixo
    cmp menu[esi], 3Eh
    je segundaOpS
    jmp terceiraOpS
    segundaOpS: ;Estava na primeira opcao, move para a segunda
        mov menu[esi], 20h
        mov menu[esi + qntColunasMenu], 3Eh
        jmp start
    terceiraOpS: ;Estava na segunda opcao, move para a terceira
        mov menu[esi + qntColunasMenu], 20h
        mov menu[esi + qntColunasMenu + qntColunasMenu], 3Eh
        jmp start
teclaW: ; Move o cursor para cima
    cmp menu[esi + qntColunasMenu + qntColunasMenu], 3Eh
    je segundaOpW 
    jmp primeiraOpW
    primeiraOpW: ;Estava na segunda opcao, move par a primeira
        mov menu[esi], 3Eh
        mov menu[esi + qntColunasMenu], 20h
        jmp start
    segundaOpW: ;Estava na terceira opcao, move para a segunda
        mov menu[esi + qntColunasMenu], 3Eh
        mov menu[esi + qntColunasMenu + qntColunasMenu], 20h
        jmp start
    
sair:
    call Clrscr
    ret

telaInicial endp

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;FUNCAO: Processar o movimento feito pelo jogador
;Recebe: matriz e dados da matriz
;       comando dado
;       sinalMapa
;Retorna: 
;	-esi: posicao do personagem
;	-sinalMapa: indica o que vai acontecer com o personagem
;	-sinalTesouro: indica se o personagem colide com um tesouro
;Requer: o jogador tenha executado um comando salvo em al
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
processaMovimento proc	

	mov bl, al		;bl recebe o comando do jogador
	
	;calcula posicao do personagem 
	;esi = yp*qntColunas + xp
    mov ax, 0
    mov esi, 0
    mov esi, yp
    mov ax, qntColunasMapa
    mul esi
    movzx esi, ax
    add esi, xp
	
	cmp bl, "a" 
    je esquerda
    cmp bl, "d"
    je direita
    cmp bl, "w"
    je cima
    cmp bl, "s"
    je baixo
    cmp bl, 20h 	;entrar no tunel
    je tunel
	mov sinalMapa,1
	jmp sair
	
	
direita:

    ;Verifica a colisão com a parede
    mov al, mapa[esi+1]
    mov sinalMapa, 1 				;Colidiu
    cmp al, "H" 					;Se for parede, termina o procedimento
    je sair
    mov sinalMapa, "d" 				;Se nao for diz que nao colidiu
    jmp sair
	
esquerda:  
    
	;Verifica colisão com a parede
    mov al, mapa[esi-1]
    mov sinalMapa, 1
    cmp al, "H"
    je sair
    mov sinalMapa, "a"
    jmp sair
 
cima:
    ;Verifica colisao com a parede
    mov al, mapa[esi-qntColunasMapa]
    mov sinalMapa, 1
    cmp al, "H"
    je sair
    mov sinalMapa, "w"
	jmp sair
    
baixo:    
    ;Verifica a colisao com a parede
    mov al, mapa[esi+qntColunasMapa]
    mov sinalMapa, 1 
    cmp al, "H" 
    je sair
    mov sinalMapa, "s"
	jmp sair

tunel:
	;Verifica se o personagem esta em uma regiao de tunel
	mov sinalMapa,1
	cmp sinalTunel, "T"
	jne sair				;não é um local onde tem tunel
	mov sinalMapa, 2
	jmp sair
	
sair:
    ret
    
processaMovimento ENDP
    

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;FUNCAO: Atualizar a parte grafica do mapa
;RECEBE: esi(Matriz) e mapa[esi](elementos)
;        Sinal do processaMovimento
;Retorna: mapa[esi](matriz do mapa atualizado)
;Requer: o jogador fez um movimeto
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
atualizaMapa proc

    call atualizaContadores

    cmp sinalMapa, "d"
    je direita
    cmp sinalMapa, "a"
    je esquerda
    cmp sinalMapa, "w"
    je cima
    cmp sinalMapa, "s"
    je baixo
	
	cmp sinalMapa,2
	je	tunel
    
direita:
    ;Troca os caracteres do mapa (movimento)
    mov al, 0
    mov al, mapa[esi]
    mov bl, 0
	
	cmp sinalTunel, 1
	je t1
	
    ;Troca de caracteres
	mov bl, mapa[esi+1]
    cmp sinalTesouro, 1 	;se for tesouro
    jne proximo1
    mov bl, 20h 			;se for tesouro vai substituir pelo espaço vazio (ideia de coleta)
	jmp continua1
	
t1: 
	mov bl,"T"				;sai de cima do tunel
	mov sinalTunel,0
	jmp continua1
proximo1:
	cmp bl,"T"
	mov bl, 20h	
	je continua1
	cmp sinalTunel,"T" 		;se for tunel
	jne continua1
	mov bl,sinalTunel
	mov sinalTunel,0

continua1:
    mov mapa[esi], bl
    mov mapa[esi+1], al
    inc xp
    jmp sair
    
esquerda:
    ;Troca os caracteres do mapa (movimento)
    mov al, 0
    mov al, mapa[esi]
    mov bl, 0

	cmp sinalTunel, 1
	je t2

    mov bl, mapa[esi-1]
    cmp bl, "o" 		;se for tesouro
    jne proximo2
    mov bl, 20h
	jmp continua2

t2:
	mov bl,"T"
	mov sinalTunel,0
	jmp continua2

proximo2:
	cmp bl,"T"
	mov bl, 20h	
	je continua2
	cmp sinalTunel,"T" 		;se for tunel
	jne continua2
    mov sinalTunel,0
	mov bl,"T" 				; se for tunel move T para bl
	
continua2:
    mov mapa[esi], bl
    mov mapa[esi-1], al
    dec xp
    jmp sair

cima:
    ;Troca os caracteres do mapa (movimento)
    mov al, 0
    mov al, mapa[esi]
    mov bl, 0
	
	cmp sinalTunel, 1
	je t3
	
    ;Troca de caracteres
    mov bl, mapa[esi-qntColunasMapa]
    cmp bl, "o" ;se for tesouro
    jne proximo3
    mov bl, 20h
	jmp continua3
	
t3:
	mov bl,"T"
	mov sinalTunel,0
	jmp continua3
proximo3:
	cmp bl,"T"
	mov bl, 20h	
	je continua3
	cmp sinalTunel,"T" ;se for tunel
	jne continua3
    mov sinalTunel,0
	mov bl,"T" ; se for tunel move T para bl

continua3:
    mov mapa[esi], bl
    mov mapa[esi-qntColunasMapa], al
    dec yp
    jmp sair

baixo:
    ;Troca os caracteres do mapa (movimento)
    mov al, 0
    mov al, mapa[esi]
    mov bl, 0
	
	cmp sinalTunel, 1
	je t4

    ;Troca de caracteres
    mov bl, mapa[esi+qntColunasMapa]
    cmp bl, "o" ;se for tesouro
    jne proximo4
	mov bl,20h
	jmp continua4
	
t4:
	mov bl,"T"
	mov sinalTunel,0
	jmp continua4

proximo4:
	cmp bl,"T"
	mov bl, 20h	
	je continua4
	cmp sinalTunel,"T" ;se for tunel
	jne continua4
    mov sinalTunel,0
	mov bl,"T" ; se for tunel move T para bl
	
continua4:
    mov mapa[esi], bl
    mov mapa[esi+qntColunasMapa], al
    inc yp
    jmp sair

tunel:
	call entraTunel
	mov sinalTunel,"T"
	jmp sair
	
sair:    
    mov sinalTesouro,0
    ret
    
atualizaMapa ENDP

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;FUNCAO: faz a atualização do mapa ao entrar no tunel
;RECEBE: mapa,posicao do personagem e array de tuneis
;Retorna: mapa atualizado, sinalTunel atualizado
;Requer: jogador apertou a tecla para entrar no tunel
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
entraTunel PROC

	;calcula para onde o personagem vai
	call procuraTunel
	
	mov xp, eax
	mov yp, ebx
	
	;Troca os caracteres do mapa (movimento)
    mov bl, 0
    mov bl, "T"
	mov mapa[esi], bl
	
	
continua:
	;calcula as novas coordenadas do personagem
    mov ax, 0
    mov esi, 0
    mov esi, yp
    mov ax, qntColunasMapa
    mul esi
    movzx esi, ax
    add esi, xp
	mov mapa[esi],"P"
	mov sinalTunel, 1
	
sair:
	ret

entraTunel ENDP

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Função: calcula a posicao do personagem ao entrar no tunel
;Recebe: esi(posicao atual do personagem), edi(ponteiro para buscar o tunel no vetor de tuneis),
;       tuneis[] (vetor de posicao dos tuneis)
;Retorna: eax(posicao x para onde o personagem irá), ebx(posicao y para onde o personagem irá)
;		  edi(posição da coordenada x do tunel no vetor de tuneis)
;Requer: jogador entre em um tunel
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
procuraTunel PROC
	mov edi, -4
	mov edx, 0
	mov eax, xp
	mov ebx,yp
	mov ecx,qntTuneis   ;(quantidade de tuneis/2)+1
	inc ecx
	
	cmp esi,tunelFinal	;esi = final
	jne L1
	cmp tesourosRestantes,0	
	jne sair
    
    call proximaFase
    jmp sair
        
L1:
	add edi,4
	mov ax,qntColunasMapa
	movzx dx,tuneis[edi+1]
	mul dx
	movzx bx,tuneis[edi]
	add ax,bx
	cmp eax,esi
	je continua1
	loop L1

	mov ecx,qntTuneis
	mov edi,-2
L2:
	add edi,4
	mov ax,qntColunasMapa
	movzx dx,tuneis[edi+1]
	mul dx
	movzx bx,tuneis[edi]
	add ax,bx
	cmp eax,esi
	je continua2
	loop L2

continua1:
	;Calcula as novas coordenadas do personagem
	movzx eax, tuneis[edi+2]	;eax = xt (coordenada x do tunel)
	movzx ebx, tuneis[edi+3]	;bl	= yt (coordenada y do tunel)
	jmp sair
continua2:
	movzx eax,tuneis[edi-2]    ;eax = xt
	movzx ebx,tuneis[edi-1]  ;ebx = yt
	jmp sair
sair:
	ret
procuraTunel ENDP

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;FUNCAO: Atualiza todos os contadores do jogo
;RECEBE: contadores de movimento e de tesouro e matriz
;Requer: jogador tenha dado um comando para haver alteracoes no mapa
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
atualizaContadores proc

    cmp sinalMapa, "d"
    je direita
    cmp sinalMapa, "a"
    je esquerda
    cmp sinalMapa, "w"
    je cima
    cmp sinalMapa, "s"
    je baixo
	cmp sinalMapa,2
	je tunel
    jmp sair
    
direita:
    inc movFeitos
    mov bl, mapa[esi+1]
    cmp bl, "o"  ;se for tesouro
    jne prox1
    dec tesourosRestantes ;Decrementa o numero de restantes
    mov sinalTesouro, 1 ;Avisa atualizaMapa que encontrou tesouro
	jmp sair

prox1:
	call colideTunel
	jmp sair
	
esquerda:    
    inc movFeitos
    mov bl, mapa[esi-1]
    cmp bl, "o" 
    jne prox2
    dec tesourosRestantes
    mov sinalTesouro, 1
    jmp sair
	
prox2:
	call colideTunel
	jmp sair

cima:
    inc movFeitos
    mov bl, mapa[esi-qntColunasMapa]
    cmp bl, "o" 
    jne prox3
    dec tesourosRestantes
    mov sinalTesouro, 1
    jmp sair
    
prox3:
	call colideTunel
	jmp sair

baixo:
    inc movFeitos
    mov bl, mapa[esi+qntColunasMapa]
    cmp bl, "o" 
    jne prox4
    dec tesourosRestantes
    mov sinalTesouro, 1
    jmp sair
    
prox4:
	call colideTunel
	jmp sair
	
tunel:
	inc movFeitos
	jmp sair
	
sair:
    ;Imprime na tela a configuracao dos contadores no formato
    ;Tesouros : tesourosRestantes
    ;Movimentos: movRestantes
    
    ;Impressao do contador de tesouros
    mov edx,0
    mov eax,0
    mov edx, OFFSET tesourosStr
    call WriteString
    mov eax, tesourosRestantes
    call WriteDec
    mov al, 0Ah
    call WriteChar
    mov al, 0Dh
    call WriteChar
    
    ;impressao do contador de movimentos
    mov edx,0
    mov eax,0
    mov edx, OFFSET movimentosStr1
    call WriteString
    movzx eax, movDificuldade
    call WriteDec
    mov al, 0Ah
    call WriteChar
    mov al, 0Dh
    call WriteChar
    mov edx, OFFSET movimentosStr2
    call WriteString
    movzx eax, movFeitos
    call WriteDec
    mov al, 0Ah
    call WriteChar
    mov al, 0Dh
    call WriteChar
    
    ret
	
atualizaContadores ENDP

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;FUNCAO: verifica se houve a colisão com o tunel
;RECEBE: al -> elemento na posicao para qual o personagem irá
;Retorna: sinalTunel atualizado
;Requer: atualizaContadores seja chamada
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
colideTunel PROC
	;Verifica se houve a colisao com o tunel
	cmp bl, "T"
	jne sair
	mov sinalTunel,"T"
sair:
	ret

colideTunel ENDP

END main
