from src.external_api import HeadHunterAPI
from src.vacancies import Vacancy
from src.file_handler import JSONFileHandler


def entry_point():
    """Основная функция, точка входа"""
    file_handler = JSONFileHandler()

    while True:
        print("Выберите пункт меню:")
        print("1. Запроса вакансий из hh.ru")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии с ключевым словом в описании")
        print("4. Добавить вакансию в файл")
        print("5. Удалить вакансию из файла")
        print("6. Выход")

        selection = input("Введите номер действия: ")

        if selection == '1':
            hh_api = HeadHunterAPI()
            query = input("Введите поисковый запрос: ")
            vacancies_number = int(input("Сколько вакансий по 10 на страницу запросить: "))
            hh_api.get_vacancies(query, vacancies_number)
            vacancies_obj = [
                Vacancy(
                    name=vac['name'],
                    company=vac.get('employer', {}).get('name'),
                    salary=vac.get('salary', {}),
                    url=vac['url'],
                    description=vac.get('snippet', {}).get('requirement')
                ) for vac in hh_api.vacancies
            ]
            vacancies_list = []
            for v in vacancies_obj:
                vacancies_list.append(v.to_dict())
            file_handler.load_vacancies_to_file(vacancies_list)
            if vacancies_list:
                print('Загрузка вакансий в файл прошла успешно!')
                print(f'Загружено вакансий в количестве: {len(vacancies_list)} ')
            else:
                print("Вакансии не найдены.")

        elif selection == '2':
            n = int(input("Введите количество вакансий для получения по зарплате: "))
            vacancies = file_handler.get_vacancies()
            sorted_vacancies = sorted(vacancies, key=lambda x: x.get('salary', 0), reverse=True)[:n]
            if sorted_vacancies:
                for v in sorted_vacancies:
                    print(v)
            else:
                print("Вакансии не найдены.")

        elif selection == '3':
            search_text = input("Введите ключевое слово для поиска в файле: ")
            vacancies = file_handler.get_vacancies(search_text)
            if vacancies:
                for v in vacancies:
                    print(v)
            else:
                print("Вакансии не найдены.")

        elif selection == '4':
            name = input("Введите название вакансии: ")
            company = input("Введите название компании: ")
            # salary_from, salary_to = input("Введите зарплату от и до в формате (3000 5000): ").split()
            # salary = {'from': int(salary_from), 'to': int(salary_to)}
            salary_from = input("Введите минимальную зарплату: ")
            salary_to = input("Введите максимальную зарплату: ")
            salary = {'from': int(salary_from) if salary_from and int(salary_from) > 0 else 0,
                      'to': int(salary_to) if salary_to and int(salary_to) > 0 else 0}
            url = input("Введите ссылку на вакансию: ")
            description = input("Введите описание вакансии")

            vacancy = Vacancy(name=name, company=company, salary=salary, url=url, description=description)
            file_handler.add_vacancy(vacancy.to_dict())
            print("Вакансия добавлена в файл.")

        elif selection == '5':
            vacancy_id = int(input("Введите ID вакансии для удаления: "))
            file_handler.delete_vacancy(vacancy_id)
            print(f"Вакансия с ID {vacancy_id} удалена из файла.")

        elif selection == '6':
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите действие от 1 до 6.")


if __name__ == "__main__":
    entry_point()
