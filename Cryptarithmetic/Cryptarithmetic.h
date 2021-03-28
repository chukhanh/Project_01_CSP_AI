#pragma once

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;

//set 1, when one character is assigned previously
struct node {
	char letter;
	int value;
};

class Cryptarithmetic {
private:
	vector<string> operand;
	vector<int> operatorOrder;
	vector<char> operators = { '+', '-', '*', '=' };
	int numOperand = 0;
public:
	int isValid(node* nodeList, const int count);
	bool permutation(int count, node* nodeList, int n);
	bool solvePuzzle();

	~Cryptarithmetic();
};

