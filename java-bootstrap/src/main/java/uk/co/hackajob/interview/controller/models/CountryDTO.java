package uk.co.hackajob.interview.controller.models;

public class CountryDTO {

    private String iso3;
    private String commonName;

    // - - - - - - - - - -
    // - - - - - - - - - -

    public CountryDTO() {
    }

    public CountryDTO(String iso3, String commonName) {
        this.iso3 = iso3;
        this.commonName = commonName;
    }

    public String getIso3() {
        return iso3;
    }

    public void setIso3(String iso3) {
        this.iso3 = iso3;
    }

    public String getCommonName() {
        return commonName;
    }

    public void setCommonName(String commonName) {
        this.commonName = commonName;
    }
}
