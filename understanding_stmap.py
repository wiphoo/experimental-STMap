#!/usr/bin/env python3
#######################################################################################
#
#	Copyright (c) 2018, Wiphoo (Terng) Methachawalit, All rights reserved.
#
#######################################################################################

#######################################################################################
#
#	GLOBAL VARIABLES
#

StMapWidth = 1920
StMapHeight = 1080

#######################################################################################
#
#	HELPER FUNCTIONS
#

def searchPixelValueInSrcStMap( pixelRedVal, pixelGreenVal, stMapWidth, stMapHeight ):
	''' in src STMap image is a image that value in red channel start from 0 to 1 in x axis
			and green channel start from 0 to 1 in y axis
		so pixel value (x, y) at (0, 0) is ( 0, 0, 0 )
			and at (1, 1) is ( 1, 1, 0 )
			
		we convert the space [0,1) to [0,width) and [0,height)
			NOTE that our pixel coordinate (0,0) is a center of pixel
	'''
	return ( ( pixelRedVal * float( stMapWidth ) ), 
				( pixelGreenVal * float( stMapHeight ) ) )

#######################################################################################
#
#	MAIN
#


#	testing get the pixel position at given pixel value
pixelRedVal = 0.5
pixelGreenVal = 0.5
print( '        pixel red/green value = {}/{}, pixel coordinate in src STMap = {}'.format( 
					pixelRedVal, pixelGreenVal,
					searchPixelValueInSrcStMap(  pixelRedVal, pixelGreenVal, StMapWidth, StMapHeight ) ) )

pixelRedVal = 0.
pixelGreenVal = 0.
print( '        pixel red/green value = {}/{}, pixel coordinate in src STMap = {}'.format( 
					pixelRedVal, pixelGreenVal,
					searchPixelValueInSrcStMap(  pixelRedVal, pixelGreenVal, StMapWidth, StMapHeight ) ) )
pixelRedVal = 1.0
pixelGreenVal = 0.5123
print( '        pixel red/green value = {}/{}, pixel coordinate in src STMap = {}'.format( 
					pixelRedVal, pixelGreenVal,
					searchPixelValueInSrcStMap(  pixelRedVal, pixelGreenVal, StMapWidth, StMapHeight ) ) )	
	
