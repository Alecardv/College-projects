#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <sstream>

using namespace std;

class BigNum{
	
	string a;

public:
	// Constructores //
	BigNum();
	BigNum(string num);
	BigNum(const char* c);
	BigNum(int num);
	BigNum(long num);
	BigNum(long long num);
	~BigNum();

	// Metodos //
	int size();
	void print();
	BigNum normalize();

	// Sobrecargas //
	// -Asignacion
	BigNum operator = (string a);
	BigNum operator = (const char* c);
	BigNum operator = (int i);
	BigNum operator = (long l);
	BigNum operator = (long long ll);

	// -Aritmeticos
	BigNum operator + (BigNum a);
	BigNum operator - (BigNum a);
	BigNum operator * (BigNum a);
	BigNum operator / (BigNum a);
	BigNum operator % (BigNum a);

	// Unarios
	BigNum operator ++ (int);
	BigNum operator -- (int);
	
	// -Comparacion
	bool operator < (BigNum &b);
	bool operator >  (const BigNum &b) const;
	/*bool operator <= (const BigNum &a) const;
	bool operator >= (const BigNum &a) const;
	bool operator == (const BigNum &a) const;
	bool operator != (const BigNum &a) const;
	*/
};

// Constructores //
BigNum::BigNum() {}

BigNum::BigNum(string num){
	(*this) = num;
}

BigNum::BigNum(const char* c){

	(*this) = string(c);
}

BigNum::BigNum(int num){
	std::ostringstream s;
	s << num;
	(*this) = s.str();
}

BigNum::BigNum(long num){
	std::ostringstream s;
	s << num;
	(*this) = s.str();
}

BigNum::BigNum(long long num){
	std::ostringstream s;
	s << num;
	(*this) = s.str();
}

BigNum::~BigNum() {}

//#####################################//
             // Metodos //
int BigNum::size(){
	return a.size();
}

void BigNum::print(){
	//for( int i = a.size() - 1; i >= 0; i-- ) putchar(a[i]);
	cout << a << endl;
}

BigNum BigNum::normalize(){
	while (true){
		if (a[0] == '0') {
			a.erase(a.begin());
			return (*this);
		}
		else return (*this);
	}
	for( int i = a.size() - 1; i > 0 && a[i] == '0'; i-- )
		a.erase(a.begin() + i);
	return (*this);
}

// Sobrecargas //

// -Asignacion
BigNum BigNum::operator = (string b){
	//cout << "string" << endl;
	this->a = b;
	return (*this);
}

BigNum BigNum::operator = (const char* c){
	//cout << "char" << endl;
	std::ostringstream s;
	s << c;
	 this->a = s.str();
	return (*this);
}

BigNum BigNum::operator = (int i){
	std::ostringstream s;
	s << i;
	(*this) = s.str();
	return (*this);
}

BigNum BigNum::operator = (long l){
	std::ostringstream s;
	s << l;
	(*this) = s.str();
	return (*this);
}

BigNum BigNum::operator = (long long ll){
	std::ostringstream s;
	s << ll;
	(*this) = s.str();
	return (*this);
}

// -Aritmeticos
BigNum BigNum::operator + (BigNum b){
	BigNum c;
	for(int i = 0, carry = 0; i<a.size() || i<b.size() || carry; i++ ) {
		carry+=(i<a.size() ? a[i]-48 : 0)+(i<b.a.size() ? b.a[i]-48 : 0);
		c.a += (carry % 10 + 48);
		carry /= 10;
	}
	return c.normalize();
}

BigNum BigNum::operator - (BigNum b){
	BigNum c;
	for( int i = 0, borrow = 0; i < a.size(); i++ ) {
		borrow = a[i] - borrow - (i < b.size() ? b.a[i] : 48);
		c.a += borrow >= 0 ? borrow + 48 : borrow + 58;
		borrow = borrow >= 0 ? 0 : 1;
	}
	return c.normalize();
}

BigNum BigNum::operator * (BigNum b){
	BigNum c("0");
	for( int i = 0, k = a[i] - 48; i < a.size(); i++, k = a[i] - 48 ) {
      while(k--) c = c + b; // ith digit is k, so, we add k times
      b.a.insert(b.a.begin(), '0'); // multiplied by 10
  }
  return c.normalize();
}

BigNum BigNum::operator / (BigNum b){
	if( b.size() == 1 && b.a[0] == '0' ) b.a[0] /= ( b.a[0] - 48 );
	BigNum c("0"), d;
	for( int i = a.size() - 1; i >= 0; i-- ) {
		c.a.insert( c.a.begin(), '0');
		c = c + a.substr( i, 1 );
		while( !( c < b ) ) c = c - b, d.a[i]++;
	}
	return d.normalize();
}

BigNum BigNum::operator % (BigNum b){
	if( b.size() == 1 && b.a[0] == '0' ) b.a[0] /= ( b.a[0] - 48 );
	BigNum c("0");
	for( int i = a.size() - 1; i >= 0; i-- ) {
		c.a.insert( c.a.begin(), '0');
		c = c + a.substr( i, 1 );
		while( !( c < b ) ) c = c - b;
	}
	return c.normalize();
}

// Unarios
BigNum BigNum::operator ++ (int){
	BigNum uno = 1;
	*this = *this + uno;
	return (*this);
}

BigNum BigNum::operator -- (int){
	BigNum uno = 1;
	*this = *this - uno;
	return (*this);
}
// -Comparacion 
bool BigNum::operator <  (BigNum &b) {
	if( a.size() != b.a.size() )
		return a.size() < b.a.size();
	for( int i = a.size() - 1; i <= 0; i-- ) if( a[i] != b.a[i] )
		return a[i] < b.a[i];
	return false;
	//b = b.normalize();
	//(*this) = (*this).normalize();
	//if ((*this).size() < b.size()) return true;
	//else return false;
}

bool BigNum::operator >  (const BigNum &b) const{
	if( a.size() != b.a.size() )
		return a.size() > b.a.size();
	for( int i = a.size() - 1; i <= 0; i-- ) if( a[i] != b.a[i] )
		return a[i] > b.a[i];
	return false;
}
/*
bool BigNum::operator <= (const BigNum &b) const{

}

bool BigNum::operator >= (const BigNum &b) const{

}

bool BigNum::operator == (const BigNum &b) const{
	return a == b.a && sign == b.sign;
}

bool BigNum::operator != (const BigNum &b) const{

}
*/
int main(int argc, char const *argv[]){
	
	BigNum a = "9999999999999999999999999999999999999999999999999999999999991";
	BigNum b = "11111111111111111111111111111111111111";
	if (a < b) {
		cout << "true" << endl;
		return 0;
	}
	cout << "false" << endl;
	//BigNum c = a/b;
	//c.print();
	return 0;
}
