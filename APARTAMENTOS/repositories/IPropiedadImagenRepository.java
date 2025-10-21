package com.example.apartamentos.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.example.apartamentos.models.PropiedadImagen;

@Repository
public interface IPropiedadImagenRepository extends JpaRepository<PropiedadImagen, Long> {

}
