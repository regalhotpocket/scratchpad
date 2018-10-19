#include <iostream>
#include <vector>
#include "List.h"

using fds::List;
using std::cout;
using std::endl;

int main(){
	auto init = []() {
		const List<int> a({ 1, 2, 3, 4, 5 });
		const List<int> b = a + 0;
		return b;
	};
	auto lessThanSix = [](int i) { return ( i < 4 ? true : false); };
	auto square = [](int i) { return i*i; };

	List<int> a = init();
	cout << "a, original: " << a << endl;
	List<int> b = a.filter(lessThanSix);
	cout << "b, filterd all larger than 3: " << b << endl;
	List<int> c = b.map(square);
	cout << "c, squared all: " << c << endl;
	List<int> d =  c + b;
	cout << "d, c + b: " << d << endl;
}