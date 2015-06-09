import flask, json
from flask import request

app = flask.Flask('trioapi')
app.config['DEBUG'] = True;


@app.route('/trioapi/v0/getTrio', methods=['GET'])
def getTrio():
    userid = request.args.get('userid')
    nReqStations = request.args.get('numRequestedStations')
    nPreArtistsPerStation = request.args.get('numPreviousArtistsPerStation')
    nPreAlbumArtsPerStation = request.args.get('numPreviousAlbumArtsPerStation')

    if not userid or not nReqStations or not nPreArtistsPerStation or not nPreAlbumArtsPerStation :
        response = json.dumps('Invalid Request')
        return response


    #getTrioStation()

    nRetStations = 1

    stationName = 'Blondie Radio'
    artistArr = []
    albumArtArr = []
    contentItem = {'source': 'PANDORA', 'location':  '2604395018315179734', 'sourceAccount': 'iTunesForRad@gmail.com', 'isPresetable':'true'}


    response = {'numReturnedStations': nRetStations,'stations': [{'itemName': stationName, 'ContentItem': contentItem, 'artistArr': artistArr,  'albumArtArr': albumArtArr},]} 

    return json.dumps(response)

#app.run(host='0.0.0.0')

