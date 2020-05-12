# Intro to Python GIS
# https://automating-gis-processes.github.io/CSC18/lessons/L6/raster-mosaic.html
import rasterio
from rasterio.merge import merge
from rasterrio.plot import show
import glob
import os
# Find all tif files from the folder where the file starts with L -letter.
dirpath = "F:/1rs/3/"
out_fp = "F:/1rs/3/mosaic.tif"
search_criteria = "*.tif"
q = os.path.join(dirpath, search_criteria)
print(q)
# List all dem files with glob() function
dem_fps = glob.glob(q)
dem_fps
src_files_to_mosaic = []
# Now we open all those files in read mode with raterio and add those files into a our
# source file list
# Merge function returns a single mosaic array and the transformation info
mosaic, out_trans = merge(src_files_to_mosaic)
show(mosaic, cmap='terrain')
out_meta = src.meta.copy()
out_meta.update({"driver": "GtIFF",
                 "height": mosaic.shape[1],
                 "width":mosaic.shape[2],
                 "transform": out_trans,
                 "crs":"+proj=utm +zone35 +ellps =GRS80 +units=m +no_defs "
        }
        )
with rasterio.open(out_fp, "w", **out_meta) as dest:
    dest.write(mosaic)




