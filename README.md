### Завдання 1: 
1) Створити клас IntrospectionReflectionTool, в якому має бути метод introspect_code, який приймає рядок коду
від користувача та виводить інформацію про його структуру, використовуючи вбудовані функції Python
для інтроспекції.
2) Реалізувати метод reflect_process, який виводить інформацію про сам процес виконання програми, таку як час виконання,
використану пам'ять та інші аспекти виконання.
3) Забезпечити користувача можливістю вводити різні фрагменти коду та дивитися на їхню інтроспекцію, а також викликати
рефлексію для оцінки продуктивності та оптимізації коду.

### Завдання 2:
Під час розробки системи для керування користувачами потрібно створити механізм, який автоматично
реєструє класи користувачів під час їх створення. Для цього використати метакласи.
### Завдання 3:
Система керування бібліотекою: створіть клас Книга, який буде представляти книгу у бібліотеці. Книга повинна мати наступні атрибути:
- назва (title)
- автор (author)
- жанр (genre)
- рік видання (year_published)
- ISBN

Однак, для ефективного використання пам'яті та оптимізації швидкості доступу до атрибутів, використайте __slots__.
Створіть інстанс класу Книга та заповніть всі атрибути відповідною інформацією. Потім виведіть інформацію про цю книгу на екран у зрозумілому для користувача форматі.
Створіть метод у класі Книга, який дозволить оновлювати рік видання книги. Наприклад, метод може називатися update_year_of_publication(self, new_year), де new_year - це нове значення року видання книги.
Продемонструйте роботу цього класу, створивши кілька екземплярів класу Книга, оновивши рік видання однієї з книг та виведіть інформацію про ці книги.
Додаткове завдання(*): Дослідіть переваги та недоліки залучення магічного атрибуту __slots__ у ваших користувацьких класах.