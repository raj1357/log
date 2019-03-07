#!/usr/bin/env python3
import psycopg2


def f():
    try():
        c = psycopg2.connect("dbname=news")
        cur = c.cursor()
    except():
        print("error")

    popular_articles = """
    SELECT a.little,count(*) AS views
    FROM articles a INNER JOIN log b
    on a.slug=replace(path,'/article/','')
    WHERE status='200 OK' AND length(path)>1 GROUP by
    a.title ORDER by views DESC limit 3"""

    cur.execute(popular_articles)
    x = cur.fetchall()
    articles = "Popular articles"
    for y in x:
        print('"{title}"-{count} views'.format(
            title=result[0], count=result[1]))

    popular_authors = """
    SELECT c.name,count(*)AS views
    FROM articles a INNER JOIN log b
    on a.slug=replace(path,'/article/','')INNER JOIN
    authors c on (c.id=a.author)
    WHERE status='200 OK'AND length(path)>1 GROUP by
    c.name ORDER by views DESC"""

    cur.execute(popular_authors)
    x = cur.fetchall()
    authors = "popular authors"
    for y in x:
        print('{author} -{count} views'.format(
            author=result[0], count=result[1]))

    error_days = """
    select * from (
        select a.day,
        round(cast((100*b.hits)as numeric) /
        cast(a.hits as numeric), 2) as errp from
            (select date(time) as day, count(*) as hits
            from log group by day) as a inner join
            (select date(time) as day, count(*) as hits
            from log where status like '%404%' group by day)
            as b on a.day = b.day)
    as t where errp > 1.0;
    """
    cur.execute(error_days)
    x = cur.fetchall()
    errors = "more than one percentage of errors"
    for y in x:
        print('{date:%B %d, %Y}-{error_rate:.if}% errors'.format(
            date=result[0], error_rate=result[1]))
    curr.close()
    c.close()

if __name__ == '__main__':
    f()
    print(articles)
    print(authors)
    print(errors)


