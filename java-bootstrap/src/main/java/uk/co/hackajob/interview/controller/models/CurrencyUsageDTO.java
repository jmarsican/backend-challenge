package uk.co.hackajob.interview.controller.models;

import java.util.ArrayList;
import java.util.List;

public class CurrencyUsageDTO {

    private String code;
    private String name;
    private List<CountryDTO> countries = new ArrayList<>();

    private int usages;
    
    // - - - - - - - - - - -
    // - - - - - - - - - - -

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getUsages() {
        return getCountries().size();
    }

    public List<CountryDTO> getCountries() {
        return countries;
    }

    public void setCountries(List<CountryDTO> countries) {
        this.countries = countries;
    }

}
