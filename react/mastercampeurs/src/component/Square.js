import React from 'react';
import {StyleSheet, Text, View} from 'react-native';

class Square extends React.Component {
  render() {
    return (
      <View style={{backgroundColor: 'red'}}>
        <Text>{this.props.title}</Text>
      </View>
    );
  }
}

const styles = StyleSheet.create();

export default Square;
