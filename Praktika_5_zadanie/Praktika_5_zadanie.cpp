#include <iostream>
using namespace std;
class Mass
{
public:
	int len = 0;
	int* massive = new int;

	void Adding(int index) 
	{
		int* newMass = new int[len + 1];
		for (int i = 0; i < len; i++)
		{
			newMass[i] = massive[i];
		}
		newMass[len] = index;
		len++;
		delete[] massive;
		massive = newMass;
	}
	void CurrentNumbers() 
	{
		cout << "Current amount of numbers: " << len << endl;
	}
	void Index(int i) 
	{
		cout << "Element by Index " << i << ": " << massive[i] << endl;
	}
	void ChangebyIndex(int i, int new_index) 
	{
		massive[i] = new_index;
	}
	void DeletebyIndex(int i) 
	{
		int* newMass = new int[len - 1];
		int flag = 0;
		for (int j = 0; j < len; j++)
		{
			if (j == i) 
			{
				flag++;
				continue;
			}
			newMass[j - flag] = massive[j];
		}
		delete massive;
		len--;
		massive = newMass;
	}
	void InsertbyIndex(int i, int index) 
	{
		int* newMass = new int[len + 1];
		int flag = 0;
		for (int j = 0; j < len + 1; j++)
		{
			if (j == i) 
			{
				flag++;
				newMass[i] = index;
				continue;
			}
			newMass[j] = massive[j - flag];
		}
		delete massive;
		len++;
		massive = newMass;
	}

}
int main()
{
	setlocale(LC_ALL, "russian");
	Mass mass;
	mass.Adding(-1);
	mass.Adding(2);
	mass.Adding(3);
	mass.CurrentNumbers();
	mass.Index(0);
	mass.ChangebyIndex(0, 1);
	mass.Index(0);
	mass.DeletebyIndex(0);
	mass.CurrentNumbers();
	mass.Index(0);
	mass.InsertbyIndex(0, 1);
	mass.Index(0);




	
}
