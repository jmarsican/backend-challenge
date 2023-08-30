package uk.co.hackajob.interview.persistence;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

@Entity
@Table(name = "currency", schema = "hackajob_global_currencies", catalog = "postgres")
public class Currency {
    
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    @Column(name = "id")
    private int id;

    @Basic
    @Column(name = "code")
    private String code;

    @Basic
    @Column(name = "name")
    private String name;

    @ManyToMany(cascade = CascadeType.ALL, targetEntity = Country.class)
    @JoinTable(
            schema = "hackajob_global_currencies",
            catalog = "hackajob",
            name = "country_currency",
            joinColumns = @JoinColumn(name = "currency_id"),
            inverseJoinColumns = @JoinColumn(name = "country_id")
    )
//    @ManyToMany(cascade = CascadeType.ALL, mappedBy = "currencies", targetEntity = Country.class)
    private Set<Country> countries = new HashSet<>();

    // - - - - - - - - - -
    // - - - - - - - - - -

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

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

    public Set<Country> getCountries() {
        return countries;
    }

//    public void setCountries(Set<Country> countries) {
//        this.countries = countries;
//    }

    public void addCountry(Country country) {
        countries.add(country);
        country.getCurrencies().add(this);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Currency that = (Currency) o;
        return id == that.id && Objects.equals(code, that.code) && Objects.equals(name, that.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, code, name);
    }


    @Override
    public String toString() {
        return "Currency{" +
                "id=" + id +
                ", code='" + code + '\'' +
//                ", name='" + name + '\'' +
//                ", countries=" + countries +
                '}';
    }
}
