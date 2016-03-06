#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <sstream>

using namespace std;

class BigNum{

	string a;
	int sign;

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
	BigNum chSign();
	BigNum normalize(int newSign);
	void print();

	// Sobrecargas //
	// - Asignacion:
	void operator = (string a);
	void operator = (const char* c);
	BigNum operator = (int i);
	BigNum operator = (long l);
	BigNum operator = (long long ll);

	// - Aritmeticos:
	BigNum operator + (BigNum a);
	BigNum operator - (BigNum a);
	BigNum operator * (BigNum a);
	BigNum operator / (BigNum a);
	BigNum operator % (BigNum a);

    // - Unarios:
	BigNum operator ++ (int);
	BigNum operator -- (int);

	// - Comparacion:
	bool operator <  (const BigNum &b) const;
	bool operator >  (const BigNum &b) const;
	bool operator == (const BigNum &a) const;
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

BigNum BigNum::chSign(){
	sign *= -1;
	return (*this);
}

BigNum BigNum::normalize(int newSign) {
	for( int i = a.size() - 1; i > 0 && a[i] == '0'; i-- )
		a.erase(a.begin() + i);
	sign = ( a.size() == 1 && a[0] == '0' ) ? 1 : newSign;
	return (*this);
}

void BigNum::print(){
	if( sign == -1 ) putchar('-');
	for( int i = a.size() - 1; i >= 0; i-- ) putchar(a[i]);
}


// Sobrecargas //

// -Asignacion
void BigNum::operator = (string b){
	a = b[0] == '-' ? b.substr(1) : b;
	reverse( a.begin(), a.end() );
	this->normalize( b[0] == '-' ? -1 : 1 );
}

void BigNum::operator = (const char* c){
	string b = string(c);
	a = b[0] == '-' ? b.substr(1) : b;
	reverse( a.begin(), a.end() );
	this->normalize( b[0] == '-' ? -1 : 1 );
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
	if( sign != b.sign ) return (*this) - b.chSign();
	BigNum c;
	for(int i = 0, carry = 0; i<a.size() || i<b.size() || carry; i++ ) {
		carry+=(i<a.size() ? a[i]-48 : 0)+(i<b.a.size() ? b.a[i]-48 : 0);
		c.a += (carry % 10 + 48);
		carry /= 10;
	}
	return c.normalize(sign);
}

BigNum BigNum::operator - (BigNum b){
	if( sign != b.sign ) return (*this) + b.chSign();
	int s = sign; sign = b.sign = 1;
	if( (*this) < b ) return ((b - (*this)).chSign()).normalize(-s);
	BigNum c;
	for( int i = 0, borrow = 0; i < a.size(); i++ ) {
		borrow = a[i] - borrow - (i < b.size() ? b.a[i] : 48);
		c.a += borrow >= 0 ? borrow + 48 : borrow + 58;
		borrow = borrow >= 0 ? 0 : 1;
	}
	return c.normalize(s);
}

BigNum BigNum::operator * (BigNum b){
	BigNum c("0");
	for( int i = 0, k = a[i] - 48; i < a.size(); i++, k = a[i] - 48 ) {
      while(k--) c = c + b;
      b.a.insert(b.a.begin(), '0');
  }
  return c.normalize(sign * b.sign);
}

BigNum BigNum::operator / (BigNum b){
	if( b.size() == 1 && b.a[0] == '0' ) b.a[0] /= ( b.a[0] - 48 );
	BigNum c("0"), d;
	for( int j = 0; j < a.size(); j++ ) d.a += "0";
		int dSign = sign * b.sign; b.sign = 1;
	for( int i = a.size() - 1; i >= 0; i-- ) {
		c.a.insert( c.a.begin(), '0');
		c = c + a.substr( i, 1 );
		while( !( c < b ) ) c = c - b, d.a[i]++;
	}
	return d.normalize(dSign);
}

BigNum BigNum::operator % (BigNum b){
	if( b.size() == 1 && b.a[0] == '0' ) b.a[0] /= ( b.a[0] - 48 );
	BigNum c("0");
	b.sign = 1;
	for( int i = a.size() - 1; i >= 0; i-- ) {
		c.a.insert( c.a.begin(), '0');
		c = c + a.substr( i, 1 );
		while( !( c < b ) ) c = c - b;
	}
	return c.normalize(sign);
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
bool BigNum::operator <  (const BigNum &b) const{
	if( sign != b.sign ) return sign < b.sign;
	if( a.size() != b.a.size() )
		return sign == 1 ? a.size() < b.a.size() : a.size() > b.a.size();
	for( int i = a.size() - 1; i >= 0; i-- ) if( a[i] != b.a[i] )
		return sign == 1 ? a[i] < b.a[i] : a[i] > b.a[i];
	return false;
}

bool BigNum::operator >  (const BigNum &b) const{
	if( sign != b.sign ) return sign > b.sign;
	if( a.size() != b.a.size() )
		return sign == 1 ? a.size() > b.a.size() : a.size() < b.a.size();
	for( int i = a.size() - 1; i <= 0; i-- ) if( a[i] != b.a[i] )
		return sign == 1 ? a[i] > b.a[i] : a[i] < b.a[i];
	return false;
}

bool BigNum::operator == (const BigNum &b) const{
	return a == b.a && sign == b.sign;
}
