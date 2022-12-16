#include <iostream>
#include <vector>


int main() {

    setlocale(LC_ALL, "russian");

    std::vector<int> vector;

    vector.reserve(32); // задаём вместимость массива

    vector.resize(5); // изменение кол-ва элементов

    std::cout << "Вместимость массива: " << vector.capacity() << std::endl ;

    for (size_t i = 2; i <= 8; i++) 
    {
        vector.push_back(i); // добавление элемента в конец массива
    }

    vector.insert(vector.begin() + 5, 1); // сдвиг и добавление элементов (в данном случае сдвиг на одни элемент вперёд)

    vector.erase(vector.begin(), vector.begin() + 5); // удаление элементов от и до

    for (size_t i = 0; i < vector.size(); i++) {
        
        std::cout << vector[i] << std::endl; // получение элемента по индексу

        vector[i] = -1; // оператор присваивания
    }

    vector.shrink_to_fit(); // удаляет все незаполненные элементы массива

    std::cout << "Вместимость полсе shrink_to_fit: " << vector.capacity() << std::endl;

    vector.clear(); // удаление всех элементов массива

    vector.shrink_to_fit();
    std::cout << "Вместимость полсе clear и shrink_to_fit: " << vector.capacity() << std::endl;
 
    vector.emplace_back(4); // создание нового элемента в конце массива

    std::cout << "Новый элемент созданный в конце массива при помощи emlpace_back" << vector[0];


}