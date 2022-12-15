#include <iostream>
#include <string>
#include <fstream>
#define N 100



std::string Toupper(std::string slova)
{
	bool flag = true;
	std::string symbols, str;
	const char* gl = "аеёиоуэюя";
	for (int i = 0; i < slova.size() - 1; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			if (slova[i] == gl[j])
			{
				for (int k = 0; k < 10; k++)
				{
					if ((slova[i + 1] == gl[k]) && (slova[i + 1] != ' '))
					{
						slova[i] = toupper(slova[i]);
						slova[i + 1] = toupper(slova[i + 1]);
						flag = false;
						symbols += slova[i];
						symbols += slova[i + 1];

					}
				}
			}
		}
	}
	str = slova + "(" + symbols + ")";
	if (flag)
	{
		return slova;
	}
	else
	{
		return str;
	}


}

int main()
{
	setlocale(LC_ALL, "Russian");
	std::string str, slovo, slova[N], answer;
	std::ofstream fout;
	std::ifstream F;
	F.open("input.txt");
	fout.open("output.txt");
	int j = 0;

	while (getline(F, answer))
	{
		answer += "\n";
		str += answer;

	}





	for (int i = 0; i < str.size(); i++)
	{
		if (str[i] != ' ')
		{
			slovo += str[i];
		}
		if(str[i] == ' ')
		{
			slova[j] = slovo;
			slova[j] = Toupper(slova[j]) + " ";
			std::cout << slova[j] << std::endl;
			fout << slova[j];
			slovo = "";
			j++;

		}
	}



	fout.close();
	F.close();
}