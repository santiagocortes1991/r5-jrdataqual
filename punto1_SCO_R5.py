import json
import csv

# Abre el archivo y lee su contenido
with open('taylor_swift_spotify.json', 'r') as file:
    data = json.load(file)


# Convertir "key" y "time_signature" a flotantes
for album in data.get('albums', []):
    for track in album.get('tracks', []):
        if track['audio_features']['key'] is not None:
            track['audio_features']['key'] = float(track['audio_features']['key'])
        if track['audio_features']['time_signature'] is not None:
            track['audio_features']['time_signature'] = float(track['audio_features']['time_signature'])

# Abrir un archivo CSV para escribir
csv_filename = 'dataset.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    # Definir las columnas del CSV
    fieldnames = [
        "disc_number", "duration_ms", "explicit", "track_number", "track_popularity",
        "track_id", "track_name", "audio_features.danceability", "audio_features.energy",
        "audio_features.key", "audio_features.loudness", "audio_features.mode",
        "audio_features.speechiness", "audio_features.acousticness",
        "audio_features.instrumentalness", "audio_features.liveness", "audio_features.valence",
        "audio_features.tempo", "audio_features.id", "audio_features.time_signature",
        "artist_id", "artist_name", "artist_popularity", "album_id", "album_name",
        "album_release_date", "album_total_tracks"
    ]

    # Crear el escritor CSV
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Escribir el encabezado del CSV
    writer.writeheader()

    # Iterar sobre artistas, álbumes y pistas y escribir en el archivo CSV
    for album in data.get('albums', []):
        for track in album.get('tracks', []):
            row_data = {
                "disc_number": track.get("disc_number"),
                "duration_ms": track.get("duration_ms"),
                "explicit": track.get("explicit"),
                "track_number": track.get("track_number"),
                "track_popularity": track.get("track_popularity"),
                "track_id": track.get("track_id"),
                "track_name": track.get("track_name"),
                "audio_features.danceability": track.get("audio_features", {}).get("danceability"),
                "audio_features.energy": track.get("audio_features", {}).get("energy"),
                "audio_features.key": track.get("audio_features", {}).get("key"),
                "audio_features.loudness": track.get("audio_features", {}).get("loudness"),
                "audio_features.mode": track.get("audio_features", {}).get("mode"),
                "audio_features.speechiness": track.get("audio_features", {}).get("speechiness"),
                "audio_features.acousticness": track.get("audio_features", {}).get("acousticness"),
                "audio_features.instrumentalness": track.get("audio_features", {}).get("instrumentalness"),
                "audio_features.liveness": track.get("audio_features", {}).get("liveness"),
                "audio_features.valence": track.get("audio_features", {}).get("valence"),
                "audio_features.tempo": track.get("audio_features", {}).get("tempo"),
                "audio_features.id": track.get("audio_features", {}).get("id"),
                "audio_features.time_signature": track.get("audio_features", {}).get("time_signature"),
                "artist_id": data.get("artist_id"),
                "artist_name": data.get("artist_name"),
                "artist_popularity": data.get("artist_popularity"),
                "album_id": album.get("album_id"),
                "album_name": album.get("album_name"),
                "album_release_date": album.get("album_release_date"),
                "album_total_tracks": album.get("album_total_tracks"),
            }

            # Escribir la fila en el CSV
            writer.writerow(row_data)

print(f'Archivo CSV "{csv_filename}" creado exitosamente.')