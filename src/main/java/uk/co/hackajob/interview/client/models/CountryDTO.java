package uk.co.hackajob.interview.client.models;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.HashMap;
import java.util.Map;

public class CountryDTO {

    @JsonProperty(value = "cca3")
    private String iso3;

    private NameDTO name;
    
    private Map<String, CurrencyDTO> currencies = new HashMap<>();

    // - - - - - - - - - -
    // - - - - - - - - - - 

    public String getIso3() {
        return iso3;
    }

    public void setIso3(String iso3) {
        this.iso3 = iso3;
    }

    public NameDTO getName() {
        return name;
    }

    public void setName(NameDTO name) {
        this.name = name;
    }

    public Map<String, CurrencyDTO> getCurrencies() {
        return currencies;
    }

    public void setCurrencies(Map<String, CurrencyDTO> currencies) {
        this.currencies = currencies;
    }

    @Override
    public String toString() {
        return "CountryDTO{" +
                "iso3='" + iso3 + '\'' +
                ", name=" + name +
                ", currencies=" + currencies +
                '}';
    }
}
