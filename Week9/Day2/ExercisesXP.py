

import os
import urllib.request
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker


# --------------------------------------------
# Download Database
# --------------------------------------------
def download_db():
    if not os.path.exists("chinook.db"):
        print("Downloading Chinook database...")
        url = "https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"
        urllib.request.urlretrieve(url, "chinook.db")
        print("Download complete.\n")
    else:
        print("Database already exists.\n")


# --------------------------------------------
# Create Connection + Reflect Database
# --------------------------------------------
def create_connection():
    engine = create_engine("sqlite:///chinook.db")
    connection = engine.connect()

    metadata = sqlalchemy.MetaData()
    metadata.reflect(engine)

    Base = automap_base(metadata=metadata)
    Base.prepare()

    Session = sessionmaker(bind=engine)
    session = Session()

    return engine, Base, session


# --------------------------------------------
# Exercise 2 – Table Names
# --------------------------------------------
def get_table_names(engine):
    metadata = sqlalchemy.MetaData()
    metadata.reflect(engine)
    return list(metadata.tables.keys())


# --------------------------------------------
# Exercise 3 – First 3 Tracks
# --------------------------------------------
def first_three_tracks(Base, session):
    Track = Base.classes.tracks

    query = session.query(
        Track.TrackId,
        Track.Name,
        Track.UnitPrice
    ).limit(3)

    return pd.DataFrame(query.all(), columns=["TrackId", "Name", "UnitPrice"])


# --------------------------------------------
# Exercise 4 – First 20 Tracks + Album
# --------------------------------------------
def first_twenty_tracks_with_album(Base, session):
    Track = Base.classes.tracks
    Album = Base.classes.albums

    query = (
        session.query(Track.Name, Album.Title)
        .join(Album, Track.AlbumId == Album.AlbumId)
        .limit(20)
    )

    return pd.DataFrame(query.all(), columns=["Track Name", "Album Title"])


# --------------------------------------------
# Exercise 5 – First 10 Track Sales
# --------------------------------------------
def first_ten_track_sales(Base, session):
    Track = Base.classes.tracks
    InvoiceItem = Base.classes.invoice_items

    query = (
        session.query(Track.Name, InvoiceItem.Quantity)
        .join(InvoiceItem, Track.TrackId == InvoiceItem.TrackId)
        .limit(10)
    )

    return pd.DataFrame(query.all(), columns=["Track Name", "Quantity Sold"])


# --------------------------------------------
# Exercise 6 – Top 10 Tracks Sold
# --------------------------------------------
def top_ten_tracks_sold(Base, session):
    Track = Base.classes.tracks
    InvoiceItem = Base.classes.invoice_items

    query = (
        session.query(
            Track.Name,
            func.sum(InvoiceItem.Quantity).label("Total Sold")
        )
        .join(InvoiceItem, Track.TrackId == InvoiceItem.TrackId)
        .group_by(Track.Name)
        .order_by(func.sum(InvoiceItem.Quantity).desc())
        .limit(10)
    )

    return pd.DataFrame(query.all(), columns=["Track Name", "Total Sold"])


# --------------------------------------------
# Exercise 7 – Top 10 Selling Artists
# --------------------------------------------
def top_ten_artists(Base, session):
    Artist = Base.classes.artists
    Album = Base.classes.albums
    Track = Base.classes.tracks
    InvoiceItem = Base.classes.invoice_items

    query = (
        session.query(
            Artist.Name,
            func.sum(InvoiceItem.Quantity).label("Total Sold")
        )
        .join(Album, Artist.ArtistId == Album.ArtistId)
        .join(Track, Album.AlbumId == Track.AlbumId)
        .join(InvoiceItem, Track.TrackId == InvoiceItem.TrackId)
        .group_by(Artist.Name)
        .order_by(func.sum(InvoiceItem.Quantity).desc())
        .limit(10)
    )

    return pd.DataFrame(query.all(), columns=["Artist Name", "Total Sold"])


# ============================================
# Run Everything
# ============================================

if __name__ == "__main__":

    download_db()
    engine, Base, session = create_connection()

    print("===== TABLE NAMES =====")
    print(get_table_names(engine))
    print()

    print("===== FIRST 3 TRACKS =====")
    print(first_three_tracks(Base, session))
    print()

    print("===== FIRST 20 TRACKS + ALBUM =====")
    print(first_twenty_tracks_with_album(Base, session))
    print()

    print("===== FIRST 10 TRACK SALES =====")
    print(first_ten_track_sales(Base, session))
    print()

    print("===== TOP 10 TRACKS SOLD =====")
    print(top_ten_tracks_sold(Base, session))
    print()

    print("===== TOP 10 SELLING ARTISTS =====")
    print(top_ten_artists(Base, session))
    print()