function initMap() {
    const map = L.map('map', { maxZoom: 22, preferCanvas: true }).setView([40.33693644909328, -75.92738244721485], 13);

    const mapboxAccount = 'mapbox';
    const mapboxStyle = 'dark-v11';
    const mapboxToken = 'pk.eyJ1IjoibWp1bWJlLXRlc3QiLCJhIjoiY2w3ZTh1NTIxMTgxNTQwcGhmODU2NW5kaSJ9.pBPd19nWO-Gt-vTf1pOHBA';
    L.tileLayer(`https://api.mapbox.com/styles/v1/${mapboxAccount}/${mapboxStyle}/tiles/256/{z}/{x}/{y}@2x?access_token=${mapboxToken}`, {
        maxZoom: 19,
        attribution: '© <a href="https://www.mapbox.com/about/maps/">Mapbox</a> © <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong><a href="https://www.mapbox.com/map-feedback/" target="_blank">Improve this map</a></strong>',
    }).addTo(map);

    map.FLayer = L.geoJSON(null, {
        style: {
            fillColor: '#EB0000',
            fillOpacity: 0.9,
            stroke: false,
        },
    }).addTo(map);

    return map;
}

function risklevel(value) {
    var crash = value;
    var level = 'low';  // Default fill color
    if (crash > 0.5 && crash < 1) {
        level = 'middle';  // Red fill color for large crashs
    } else if (crash > 1) {
        level = 'high';  // Yellow fill color for medium crashs
    }
    return level;
};


function showFonMap(map) {
    fetch('./test.geojson')
        .then(response => {
            // Parse the response into a JavaScript object
            return response.json();
        })
        .then(geojson => {
            // Save the resulting object as a variable
            const dataGeojson = {
                type: 'FeatureCollection',
                features: geojson.features,
            };
            // Add the data GeoJSON points to the map as markers
            map.FLayer = L.geoJSON(dataGeojson.features, {
                style: function (feature) {
                    var crash = feature.properties.V1;
                    var fillColor = '#F7ECDE';  // Default fill color
                    var weight = 1
                    if (crash > 0.5 && crash < 1) {
                        fillColor = '#FAC213';  // Red fill color for large crash
                        weight = 1.5
                    } else if (crash > 1) {
                        fillColor = '#D61C4E';  // Yellow fill color for medium crashs
                        weight = 2
                    }
                    return {
                        fillColor: fillColor,
                        color: fillColor,  // Border color
                        weight: weight,  // Border width
                        opacity: 1,  // Border opacity
                        fillOpacity: 0.6  // Fill opacity
                    };
                },
                onEachFeature: function (feature, layer) {
                    // Set the clickable buffer for each feature layer
                    layer.options.clickableBuffer = 10;
                }
            }).addTo(map)
                .eachLayer(function (layer) {
                    layer.bindTooltip(`Risk Value: ${risklevel(layer.feature.properties.V1)} <br> Click to see more!!`);
                });

            // Click
            map.FLayer.addEventListener('click', (evt) => {
                // Information Variable
                var info = evt.sourceTarget.feature.properties

                if (map.hLayer !== undefined) {
                    map.removeLayer(map.hLayer);
                }
                map.hLayer = L.marker(evt.latlng)
                    .bindTooltip(`Risk level:${risklevel(info.V1)} <br> 
            Risk Value: ${info.V1} <br> 
            Daily Truck Volume: ${info.DLY_TRK_VM} <br> 
            Truck %: ${info.TRK_PCT} <br> 
            Daily Traffic Volume: ${info.DLY_VMT} <br> 
            Street Length: ${info.SEG_LNGTH_} m`, {
                        permanent: true
                    })
                    .addTo(map);

                map.setView(evt.latlng, 15);

                //close tooltip
                map.hLayer.addEventListener('click', function (e) {
                    if (map.hLayer !== undefined) {
                        map.removeLayer(map.hLayer);
                    };
                })
            });


        })
};




const map = initMap();
showFonMap(map);
