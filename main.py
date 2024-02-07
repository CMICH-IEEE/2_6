#Created on Sun Feb  4 18:17:24 2024



#@author: Samuel Lobert 

#Description: To prepare for the 2024 Superbowl betweeen the 49ers and the Chiefs, find who wins through web scraping. 

# Import the necessary libraries





import requests

import time

from bs4 import BeautifulSoup

import csv



def main():

#Call the webscraping function and then the dataProcessing method 

#If you need to run this multiple times it might be best to comment out the webscraping function so it doesn't continuously run. 

    webScraping()

    dataProcessing()



def webScraping():

    # Define the URL of the webpage to scrape

    url = "https://www.pro-football-reference.com/teams/kan/2023.htm"



    # Send a GET request to the URL

    response = requests.get(url)



    # Check if the request was successful (status code 200)

    if response.status_code == 200:

        # Parse the HTML content of the webpage

        soup = BeautifulSoup(response.content, "html.parser")



        # Find the table containing team stats

        table = soup.find("table", {"id": "team_stats"})



        # Check if the table is found

        if table:

            # Create a CSV file to write the scraped data

            with open("chiefs_2023_stats.csv", "w", newline="") as csvfile:

                writer = csv.writer(csvfile)



                # Write the header row

                header_row = [th.text for th in table.find("thead").find_all("th")]

                writer.writerow(header_row)



                # Write the data rows

                data_rows = table.find("tbody").find_all("tr")

                for row in data_rows:

                    data = [td.text for td in row.find_all("td")]

                    writer.writerow(data)



            print("Data has been scraped and saved to chiefs_2023_stats.csv.")

        else:

            print("Table containing team stats not found on the webpage.")

    else:

        print("Failed to retrieve webpage. Status code:", response.status_code)



    # Don't call requests too fast. A short wait is required 

    time.sleep(5)



    #Repeat the code for the 49ers Data:

    # Define the URL of the webpage to scrape

    url = "https://www.pro-football-reference.com/teams/sfo/2023.htm"



    # Send a GET request to the URL

    response = requests.get(url)



    # Check if the request was successful (status code 200)

    if response.status_code == 200:

        # Parse the HTML content of the webpage

        soup = BeautifulSoup(response.content, "html.parser")



        # Find the table containing team stats

        table = soup.find("table", {"id": "team_stats"})



        # Check if the table is found

        if table:

            # Create a CSV file to write the scraped data

            with open("niners_2023_stats.csv", "w", newline="") as csvfile:

                writer = csv.writer(csvfile)



                # Write the header row

                header_row = [th.text for th in table.find("thead").find_all("th")]

                writer.writerow(header_row)



                # Write the data rows

                data_rows = table.find("tbody").find_all("tr")

                for row in data_rows:

                    data = [td.text for td in row.find_all("td")]

                    writer.writerow(data)



            print("Data has been scraped and saved to niners_2023_stats.csv.")

        else:

            print("Table containing team stats not found on the webpage.")

    else:

        print("Failed to retrieve webpage. Status code:", response.status_code)   



def dataProcessing():

    # Define the file path

    chiefs_file_path = "chiefs_2023_stats.csv"

    niners_file_path = "niners_2023_stats.csv"



    # Initialize empty lists to store the headers and data

    headers = []



    # Open the CSV file and read its contents

    with open(chiefs_file_path, "r", newline="") as csvfile:

        reader = csv.reader(csvfile)



        # Read the header row

        headers = next(reader)



        # Read the data row

        chiefs_data = next(reader)



    # Remove empty strings from the headers list

    headers = [header for header in headers if header.strip() != ""]



    trueHeaders = headers[6:]



    # Print the headers

    print("Headers:", trueHeaders)



    # Print the data

    print("Chiefs Data:", chiefs_data)



    #Create a veriable to hold the score 

    chiefsScore = 0 

    ninersScore = 0 

    #Create a list for the values we care about

    importantIndex = []



    for i in trueHeaders:

        #get the index of the points scored

        if i == 'PF':

            pointsScoredIndex = trueHeaders.index(i)

            importantIndex.append(pointsScoredIndex)

            print("The points scored = ", pointsScoredIndex)



        #Get the index of offensive yards per play 

        if i == 'Y/P':

            yardsPerOffensivePlay = trueHeaders.index(i)

            importantIndex.append(yardsPerOffensivePlay)

            print("The offense gets ", pointsScoredIndex, ' yards per play')



        #Get the index of number of turnovers allowed by the offense 

        if i == 'TO':

            turnOvers = trueHeaders.index(i)

            importantIndex.append(turnOvers)

            print("The index of TO is = ", turnOvers)



        #Get the index of percent of scoring drives

        if i == 'Sc%':

            scIndex = trueHeaders.index(i)

            importantIndex.append(scIndex)

            print("The SC% index is = ", scIndex)



        #Get the index of number of points per drive  

        if i == 'Pts':

            pointsPerDrive = trueHeaders.index(i)

            importantIndex.append(pointsPerDrive)

            print("The points scored per drive is = ", pointsPerDrive)



    print(importantIndex)





    # Open the CSV for the 49ers data file and read its contents

    with open(niners_file_path, "r", newline="") as csvfile2:

        reader = csv.reader(csvfile2)



        # Read the header row

        headers = next(reader)



        # Read the data row

        niners_data = next(reader)



    #compare the data and pick the best team 

    print("The len is: ", len(importantIndex))

    for i in importantIndex: 



        if chiefs_data[i] >= niners_data[i]:

            chiefsScore += 1



            print("Chiefs " , chiefs_data[i], "49ers ", niners_data[i], "Chiefs +1")

        else: 

            ninersScore += 1

            print("Chiefs " , chiefs_data[i], "49ers ", niners_data[i], "49ers +1")



        #We subtract for the team with the most turn overs    

        if i == 4: 



            if chiefs_data[i] >= niners_data[i]:

                chiefsScore -= 2

                print("Chiefs -2")

            else:

                ninersScore -= 2 

                print("49ers -2")



    if chiefsScore >= ninersScore:

        print('The cheifs will win since they scored ', chiefsScore, ' while the 49ers scored ', ninersScore)

    else: 

        print('The 49ers will win since they scored ', ninersScore, ' while the cheifs scored ', chiefsScore)



if __name__ == "__main__":

    main()
