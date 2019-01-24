/*
    Functional Data Structures

    TODO:
        allow init with vectors
        foldr/l
        sort
        access override
        cache results
*/

#include <assert.h>
#include <memory>
#include <iostream>
#include <initializer_list>
#include <functional>
#include <iterator>

namespace fds {
    template<typename T>
    struct List {
        struct Node {
            Node() {}
            Node(const T &head, const std::shared_ptr<const Node> &tail) : _value(head), _next(tail) {}
            const T _value;
            const std::shared_ptr<const Node> _next;
        };
        //Empty list
        List() {}
        //Creating a list from an array
        List(const std::initializer_list<T> &l) : _head(init(l)) {}
        //List from a node
        List(const std::shared_ptr<const Node> &n) : _head(n) {}
        //List with a new head added
        List(const T &head, const std::shared_ptr<const Node> &tail) : _head(std::make_shared<const Node>(head, tail)) {}
       
        //?
        bool isEmpty() const { return !_head; }

        //??
        T head() const {
            assert(!isEmpty());
            return _head->_value;
        }

        //???
        List tail() const {
            assert(!isEmpty());
            return List(_head->_next);
        }

        //adding an element to the front of the list
        List operator+(const T rhs) const { return List(rhs, _head); }

        //concatinate two lists together
        List operator+(const List<T> rhs) const {
            std::function<const std::shared_ptr<const Node>(const std::shared_ptr<const Node>,const std::shared_ptr<const Node>)> cat;            
            cat = [&cat](const std::shared_ptr<const Node> &lhs, const std::shared_ptr<const Node> &rhs) {
                if (!lhs)
                    return std::make_shared<const Node>(rhs->_value, rhs->_next);
                else if (!lhs->_next)
                    return std::make_shared<const Node>(lhs->_value, rhs);
                else
                    return std::make_shared<const Node>(lhs->_value, cat(lhs->_next, rhs));
            };
            return List(_head->_value, cat(_head->_next, rhs._head)); 
        }

        template<typename F>
        List filter(F f) const {
            if (isEmpty())
                return List();
            else {
                if (f(head()))
                    return head() + tail().filter(f);
                else
                    return tail().filter(f); 
            }
        }

        template<typename F>
        List map(F f) const{
            if (isEmpty())
                return List();
            else
                return f(head()) + tail().map(f);
        }

        //unfinished
        List sort() const{
            if (isEmpty())
                return List();
            else {
                //return f(head()) + tail().map(f);
            }
        }

    private:
        const std::shared_ptr<const Node> init (const std::initializer_list<T> &l){
            auto end = l.end();
            std::function<const std::shared_ptr<const Node>(const T* i)> sub;            
            sub = [&sub, &end](const T* i) {
                if (i == end)
                    return (const std::shared_ptr<const Node>) nullptr;
                else
                    return std::make_shared<const Node>(*i, sub(i+1));
            };
            return sub(l.begin()); 
        }
        
        const std::shared_ptr<const Node> _head;
    };
    //adds an element to the front of the list 
    template<class T>
    static List<T> operator+(const T &lhs, const List<T> &rhs) {
        return rhs + lhs;
    }
    //allows the list to be written to a stream
    template<class T>
    std::ostream& operator<<(std::ostream& o, const List<T>& l) {
        if(!l.isEmpty())
            o << l.head() << " " << l.tail();
        return o;
    }
}