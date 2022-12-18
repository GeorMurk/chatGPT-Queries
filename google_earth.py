# Import the necessary libraries and modules
import ee

# Initialize the Earth Engine API
ee.Initialize()

# Set the bounding box coordinates
bbox = ee.Geometry.Rectangle([-122.5, 37.5, -121.5, 38.5])

# Load the MODIS EVI and precipitation data
evi = ee.ImageCollection('MODIS/006/MOD13A1').select('EVI')
precip = ee.ImageCollection('MODIS/006/MOD11A1').select('LPE')

# Compute the VCI and SPI within the bounding box
vci = evi.mean().expression('(EVI - min) / (max - min)').clip(bbox)
spi = precip.mean().expression('(P - min) / (max - min)').clip(bbox)

# Display the VCI and SPI maps
Map.centerObject(bbox, 10)
Map.addLayer(vci, {'min': 0, 'max': 1, 'palette': 'FF0000,FFFF00,00FF00'}, 'VCI')
Map.addLayer(spi, {'min': 0, 'max': 1, 'palette': 'FF0000,FFFF00,00FF00'}, 'SPI')
