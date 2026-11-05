import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


# Этап 1.


def average_rating(movies):
    total = 0
    for movie in movies:
        total += movie["rating"]
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes):
    hours = minutes // 60
    rest = minutes % 60
    return f"{hours}ч {rest}м"


# Этап 2.


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


# Этап 3.


def print_non_comedies(movies):
    """Печатает названия всех фильмов, кроме комедий."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_above(movies, threshold=9.0):
    found = None
    index = 0
    while index < len(movies):
        if movies[index]["rating"] > threshold:
            found = movies[index]
            break
        index += 1
    else:
        print("Шедевров не найдено")
    return found


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# Этап 4.


def normalize_title(title):
    words = []
    for word in title.split():
        words.append(word[0].upper() + word[1:])
    return " ".join(words)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


# Этап 5.


def sorted_by_rating(movies):
    return sorted(movies, key=lambda movie: movie["rating"], reverse=True)


def titles_sorted_by_rating(movies):
    return [movie["title"] for movie in sorted_by_rating(movies)]


def top_n_by_rating(movies, n=3):
    top = sorted_by_rating(movies)[:n]
    return [(movie["title"], movie["rating"]) for movie in top]


# Этап 6.


def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in sorted(movie["genres"]):
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    films = {}
    for movie in movies:
        for actor in movie["actors"]:
            films[actor] = films.get(actor, []) + [movie["title"]]
    return films


def ratings_above_average(movies):
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }


# Этап 7.


def all_genres(movies):
    genres = set()
    for movie in movies:
        genres |= movie["genres"]
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)


# Этап 8.


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


# Этап 9.


def build_report(movies):
    _, _, average_age = catalog_age_stats(movies)
    top_movies = sorted_by_rating(movies)[:3]
    genre_counts = sorted(
        count_by_genre(movies).items(),
        key=lambda item: (-item[1], item[0]),
    )

    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {average_age} лет")
    print()
    print("Топ-3 фильма:")
    for movie in top_movies:
        print(f"  {format_report_line(movie)}")
    print()
    print("Фильмов по жанрам:")
    for genre, count in genre_counts:
        print(f"  {genre} — {count}")
    print()
    print("Все жанры каталога: " + ", ".join(sorted(all_genres(movies))))


def main():
    print("Фильмы не из жанра comedy:")
    print_non_comedies(movies)

    print("\nПервый фильм с рейтингом выше 9.0:")
    best = find_first_above(movies)
    print(best["title"] if best else None)
    print("Каталог без шедевров:")
    find_first_above([m for m in movies if m["rating"] <= 9.0])

    print(f"\nДлинных фильмов (>120 мин): {count_long_movies(movies)}")

    print("\nФильмы с рейтингом не ниже 8.0:")
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))

    total_minutes = sum(m["duration_min"] for m in movies if m["rating"] > 7)
    print(f"\nСуммарная длительность фильмов с рейтингом выше 7: {total_minutes} мин")
    print()
    build_report(movies)


if __name__ == "__main__":
    main()
