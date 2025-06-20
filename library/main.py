from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas as schemas, crud as crud
from schemas import Author, AuthorUpdate
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="📚 Kutubxona API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.get("/books/", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Kitob topilmadi")
    return book

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db, book_id, book)
    if not db_book:
        raise HTTPException(status_code=404, detail="Yangilash uchun kitob topilmadi")
    return db_book

@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="O'chirish uchun kitob topilmadi")
    return book



@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db, author)

@app.get("/authors/", response_model=list[Author])
def read_authors(db: Session = Depends(get_db)):
    return crud.get_authors(db)

@app.get("/authors/{author_id}", response_model=Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    author = crud.get_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Muallif topilmadi")
    return author

@app.put("/authors/{author_id}", response_model=Author)
def update_author(author_id: int, author: AuthorUpdate, db: Session = Depends(get_db)):
    db_author = crud.update_author(db, author_id, author)
    if not db_author:
        raise HTTPException(status_code=404, detail="Yangilash uchun muallif topilmadi")
    return db_author

@app.delete("/authors/{author_id}", response_model=Author)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = crud.delete_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="O‘chirish uchun muallif topilmadi")
    return author



@app.post("/genre/", response_model=schemas.Genre)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    return crud.create_genre(db, genre)


@app.get("/genre/", response_model=list[schemas.Genre])
def read_genres(db: Session = Depends(get_db)):
    return crud.get_genres(db)



@app.get("/genre/{genre_id}", response_model=schemas.Genre)
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = crud.get_book(db, genre_id)
    if not genre:
        raise HTTPException(status_code=404, detail="Janr topilmadi")
    return genre

@app.put("/genre/{genre_id}", response_model=schemas.Genre)
def update_genre(genre_id: int, genre: schemas.GenreUpdate, db: Session = Depends(get_db)):
    db_genre = crud.update_genre(db, genre_id, genre)
    if not db_genre:
        raise HTTPException(status_code=404, detail="Yangilash uchun janr topilmadi")
    return db_genre

@app.delete("/genres/{genre_id}", response_model=schemas.Genre)
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = crud.delete_genre(db, genre_id)
    if not genre:
        raise HTTPException(status_code=404, detail="O'chirish uchun Janr topilmadi")
    return genre



