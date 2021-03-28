#include "Cryptarithmetic.h"

vector<int> use(10);
const int MAX = 100;

int Cryptarithmetic::isValid(node* nodeList, const int count) {
	int* val = new int[MAX];
	for (int i = 0; i < sizeof(val); i++) {
		val[i] = 0;
	}
	int total = 0;

	for (int i = 0; i < operand.size(); i++) {
		int m = 1;
		int j, k;
		for (j = operand[i].length() - 1; j >= 0; j--) {
			char ch = operand[i][j];
			for (k = 0; k < count; k++) {
				if (nodeList[k].letter == ch)
					break;
			}
			val[i] += m * nodeList[k].value;
			m *= 10;
		}
	}

	for (int i = 0; i < operand.size() - 1; i++) {
		val[operand.size()-1] -= val[i];
	}
	if (val[operand.size() - 1] == 0)
		return 1;
	return 0;
}

bool Cryptarithmetic::permutation(int count, node* nodeList, int n) {
	if (n == count - 1) {
		for (int i = 0; i < 10; i++) {
			if (use[i] == 0) {
				nodeList[n].value = i;
				if (isValid(nodeList, count) == 1) {
					cout << "Solution found: ";
					for (int j = 0; j < count; j++)
						cout << " " << nodeList[j].letter << " = " << nodeList[j].value << endl;
					return true;
					cout << endl;
				}
			}
		}
		return false;
	}

	for (int i = 0; i < 10; i++) {
		if (use[i] == 0) {
			nodeList[n].value = i;
			use[i] = 1;
			if (permutation(count, nodeList, n + 1))
				return true;
			use[i] = 0;
		}
	}
	return false;
}

bool Cryptarithmetic::solvePuzzle() {
	ifstream in;
	string origin;
	char letter;
	string word = "";

	in.open("input.txt");
	if (!in) {
		cout << "Error 404: File input.txt not found." << endl;
		exit(0);
	}

	getline(in, origin);
	vector<char>::iterator itr;

	in.close();

	cout << origin << endl;

	for (int i = 0; i < origin.length(); i++) {

		letter = origin[i];
		itr = find(operators.begin(), operators.end(), letter);

		if (itr != operators.end()) {
			operatorOrder.push_back(itr - operators.begin());
			operand.push_back(word);
			word.clear();
			numOperand++;
		}
		else {
			word += letter;
		}
	}

	// Push the last word.
	operand.push_back(word);
	numOperand++;

	for (int i = 0; i < operand.size(); i++) {
		cout << operand[i] << " ";
	}

	int uniqueChar = 0; //Number of unique characters

	vector<int> freq(26); //There are 26 different characters

	for (int i = 0; i < operand.size(); i++) {
		for (int j = 0; j < operand[i].size(); j++) {
			++freq[operand[i][j] - 'A'];
		}
	}

	for (int i = 0; i < 26; i++)
		if (freq[i] > 0)     //whose frequency is > 0, they are present
			uniqueChar++;

	if (uniqueChar > 10) { //as there are 10 digits in decimal system
		cout << "Invalid strings";
		return 0;
	}

	node* nodeList = new node[uniqueChar];
	for (int i = 0, j = 0; i < 26; i++) {     //assign all characters found in three strings
		if (freq[i] > 0) {
			nodeList[j].letter = char(i + 'A');
			j++;
		}
	}

	cout << "Start the solution." << endl;

	return permutation(uniqueChar, nodeList, 0);
}

Cryptarithmetic::~Cryptarithmetic() {

}