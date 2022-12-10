#include <iostream>
#include <string>
#include <fstream>
#define N 300

std::string Pro(std::string line)
{
	const char *gl = "аеёиоуюэяы";
	for (int i = 0; i < line.size() - 1; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			if (line[i] == gl[j])
			{
				for (int k = 0; k < 10; k++)
				{
					if (line[i + 1] == gl[k])
					{
						line[i] = toupper(line[i]);
						line[i + 1] = toupper(line[i + 1]);
					}
				}
			}

		}
	}
	return line;

}



int main()
{
	setlocale(LC_ALL, "Russian");
	std::string line1[N];
	std::string line[N];
	std::ifstream F;
	int n;
	F.open("input.txt");
	for (int i = 0; i < sizeof(F); i++)
	{
		F >> line1[i];
	}
	for (int i = 0; i < N; i++)
	{
		if ((line1[i] != line1[N - 1]) && (line1[N - 1] == line1[N - 2]))
		{
			line[i] = line1[i];
		}
		else
		{
			n = i;
			break;
		}
	}

	for (int i = 0; i < n; i++)
	{
		line[i] = Pro(line[i]);
		std::cout << line[i] << " "; 

	}
	
}