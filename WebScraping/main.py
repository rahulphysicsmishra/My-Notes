from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())  # Makes html message more readable
    # tags = soup.find_all('h5')
    # for tag in tags:
    #     print(tag.text)

    course_cards = soup.find_all('div', class_ ='card')
    for course in course_cards:
        # print(course_cards)
        # print(course.h5)
        # print(course.h5.text)
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')