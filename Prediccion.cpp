#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

typedef struct 
{
    int buy_time;
    int sale_time;
    float result;
}prediction_data_t;

void prediction(prediction_data_t * data, float v[], int N);

void prediction(prediction_data_t * data, float v[], int N)
{
	data->sale_time=0;
	data->buy_time=0;
	data->result=0;

	for(int i=0;i<N;i++)
	{
		if(v[i] < v[data->buy_time ]) data->buy_time  = i;
		
		if(data->result < (v[i]- v[data->buy_time ])) 
		{
			data->result  = v[i]- v[data->buy_time ];
			data->sale_time=i;
		}
	}
}


int main()
{
	prediction_data_t my_data;
	float values[] = {1, 5, 4, 0.5, 4.5, 4, 1, 6, 9, 20, 0.1, 20};
	int N = 12;

	prediction(&my_data, values, N);

	cout << "Buy time: " << my_data.buy_time << endl; 
	cout << "Sale time: " << my_data.sale_time << endl; 
	cout << "Result: " << my_data.result << endl; 
	                                               

 
    return 0;
}