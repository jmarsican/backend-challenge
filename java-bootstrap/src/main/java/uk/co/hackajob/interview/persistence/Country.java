package uk.co.hackajob.interview.persistence;


import javax.persistence.*;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

@Entity
@Table(name = "country", schema = "hackajob_global_currencies", catalog = "postgres")
public class Country {

    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    @Column(name = "id")
    private int id;

    @Basic
    @Column(name = "cca3")
    private String cca3;

    @Basic
    @Column(name = "common_name")
    private String commonName;

    @Basic
    @Column(name = "official_name")
    private String officialName;

    @ManyToMany(cascade = CascadeType.ALL, mappedBy = "countries", targetEntity = Currency.class, fetch = FetchType.EAGER)
    private Set<Currency> currencies = new HashSet<>();

    // - - - - - - - - - -
    // - - - - - - - - - -

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getCca3() {
        return cca3;
    }

    public void setCca3(String cca3) {
        this.cca3 = cca3;
    }

    public String getCommonName() {
        return commonName;
    }

    public void setCommonName(String commonName) {
        this.commonName = commonName;
    }

    public String getOfficialName() {
        return officialName;
    }

    public void setOfficialName(String officialName) {
        this.officialName = officialName;
    }

    public Set<Currency> getCurrencies() {
        return currencies;
    }

    public void addCurrency(Currency currency) {
        currencies.add(currency);
        currency.getCountries().add(this);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Country that = (Country) o;
        return id == that.id && Objects.equals(cca3, that.cca3) && Objects.equals(officialName, that.officialName);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, cca3, officialName);
    }
}
