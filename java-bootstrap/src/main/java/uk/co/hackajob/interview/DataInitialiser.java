package uk.co.hackajob.interview;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import uk.co.hackajob.interview.client.CountriesClient;
import uk.co.hackajob.interview.client.models.CountryDTO;
import uk.co.hackajob.interview.client.models.CurrencyDTO;
import uk.co.hackajob.interview.persistence.Country;
import uk.co.hackajob.interview.persistence.Currency;
import uk.co.hackajob.interview.persistence.repositories.CountryRepository;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class DataInitialiser implements CommandLineRunner {

    protected final Log LOG = LogFactory.getLog(getClass());

    private final CountriesClient countriesClient;
    private final CountryRepository countryRepository;

    @Autowired
    public DataInitialiser(CountriesClient countriesClient,
                           CountryRepository countryRepository) {
        this.countriesClient = countriesClient;
        this.countryRepository = countryRepository;
    }

    @Override
    public void run(String... args) throws Exception {
        if (countryRepository.count() == 250) {
            return;
        }

        storeInitialData();
    }

    private void storeInitialData() {

        getAndStoreCountryData();

        LOG.info("Data Initialiser executed");
    }

    private void getAndStoreCountryData() {
        Set<CountryDTO> countries = countriesClient.getCountries();

        Map<String, Currency> currencyMap = new HashMap<>();
        Set<Country> countrySet = new HashSet<>();

        for (CountryDTO dto : countries) {
            Country c = new Country();
            c.setCca3(dto.getIso3());
            c.setCommonName(dto.getName().getCommon());
            c.setOfficialName(dto.getName().getOfficial());

            for (Map.Entry<String, CurrencyDTO> entry : dto.getCurrencies().entrySet()) {
                Currency currency = currencyMap.get(entry.getKey());
                if (currency == null) {
                    currency = new Currency();
                    currency.setCode(entry.getKey());
                    currency.setName(entry.getValue().getName());
                }
                c.addCurrency(currency);
                currencyMap.putIfAbsent(entry.getKey(), currency);
            }

            countrySet.add(c);
        }

        countryRepository.saveAll(countrySet);
    }
    
}