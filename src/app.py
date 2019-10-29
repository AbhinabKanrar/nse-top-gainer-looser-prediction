from service.nse_service import NseService

nseService = NseService()

if __name__ == '__main__':
    gainer_data = nseService.get_gainers()
    looser_data = nseService.get_loosers()
    print(gainer_data)
    print(looser_data)