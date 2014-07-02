import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import owslib.wmts


if __name__ == '__main__':
    url = 'http://map1c.vis.earthdata.nasa.gov/wmts-geo/wmts.cgi'
    wmts = owslib.wmts.WebMapTileService(url)

    print 'Available layers:'
    print '    ' + '\n    '.join(sorted(wmts.contents.keys()))

    layer_name = 'MODIS_Terra_CorrectedReflectance_TrueColor'

    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.add_wmts(wmts, layer_name)
    ax.coastlines()
    plt.show()
