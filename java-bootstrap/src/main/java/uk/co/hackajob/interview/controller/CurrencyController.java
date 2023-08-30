package uk.co.hackajob.interview.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import uk.co.hackajob.interview.GlobalCurrenciesApplication;
import uk.co.hackajob.interview.controller.models.CountryDTO;
import uk.co.hackajob.interview.controller.models.CurrencyUsageDTO;
import uk.co.hackajob.interview.persistence.Country;
import uk.co.hackajob.interview.persistence.Currency;
import uk.co.hackajob.interview.persistence.repositories.CountryRepository;
import uk.co.hackajob.interview.persistence.repositories.CurrencyRepository;

import java.util.*;

@RestController
@RequestMapping(value = "/currencies")
public class CurrencyController {

    private static final Logger LOG = LoggerFactory.getLogger(GlobalCurrenciesApplication.class);

    private final CountryRepository countryRepository;
    private final CurrencyRepository currencyRepository;

    @Autowired
    public CurrencyController(CountryRepository countryRepository,
                              CurrencyRepository currencyRepository) {
        this.countryRepository = countryRepository;
        this.currencyRepository = currencyRepository;
    }

    @RequestMapping(value = "/usage", method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<List<CurrencyUsageDTO>> getCurrencyUsage(@RequestParam Optional<String> code) {

        if (code.isPresent()) {
            return handleCurrencyCodePresent(code);
        }

        return getAllCurrencyUsages();

    }

    private ResponseEntity<List<CurrencyUsageDTO>> handleCurrencyCodePresent(Optional<String> code) {
        String currCode = code.get();
        if (currCode.length() == 3) {
            final Optional<Currency> currency = currencyRepository.findCurrencyByCode(code.get());
            if (currency.isPresent()) {
                List<CurrencyUsageDTO> dtos = new ArrayList<>();
                CurrencyUsageDTO dto = new CurrencyUsageDTO();
                dto.setCode(currency.get().getCode());
                dto.setName(currency.get().getName());
                for (Country c : currency.get().getCountries()) {
                    dto.getCountries().add(new CountryDTO(c.getCca3(), c.getCommonName()));
                }
                dto.getCountries().sort(Comparator.comparing(CountryDTO::getIso3));
                dtos.add(dto);
                return new ResponseEntity<>(dtos, HttpStatus.OK);
            } else {
                return new ResponseEntity<>(HttpStatus.NOT_FOUND);
            }
        } else {
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }
    }

    private ResponseEntity<List<CurrencyUsageDTO>> getAllCurrencyUsages() {
        List<Country> countries = countryRepository.findAll();
        Map<Currency, List<Country>> currencyCountryMap = new HashMap<>();
        for (Country country : countries) {
            for (Currency currency : country.getCurrencies()) {
                currencyCountryMap.putIfAbsent(currency, new ArrayList<>());
                currencyCountryMap.get(currency).add(country);
            }
        }

        List<CurrencyUsageDTO> dtos = new ArrayList<>();
        for (Map.Entry<Currency, List<Country>> entry : currencyCountryMap.entrySet()) {
            CurrencyUsageDTO dto = new CurrencyUsageDTO();
            dto.setCode(entry.getKey().getCode());
            dto.setName(entry.getKey().getName());
            for (Country c : entry.getValue()) {
                dto.getCountries().add(new CountryDTO(c.getCca3(), c.getCommonName()));
            }
            dto.getCountries().sort(Comparator.comparing(CountryDTO::getIso3));
            dtos.add(dto);
        }

        dtos.sort(Comparator.comparing(CurrencyUsageDTO::getUsages).reversed().thenComparing(CurrencyUsageDTO::getCode));

        return new ResponseEntity<>(dtos, HttpStatus.OK);
    }
}
